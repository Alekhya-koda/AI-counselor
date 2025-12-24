import json
import os
import uuid
from datetime import datetime, timezone
from pathlib import Path

from openai import OpenAI


DEFAULT_SYSTEM_PROMPT = (
    "You are <Assistant>, a warm, human-sounding, deeply empathetic mental-therapy assistant. "
    "You remember conversation context and respond only within that context. "
    "Do NOT include or fabricate any <Human> responses or tags (e.g., '<Human>', 'Human:'). "
    "Your tone should feel natural (use contractions, vary phrasing), supportive, and non-judgmental—"
    "avoid robotic or generic boilerplate. "
    "Use reflective listening: briefly summarize what you heard and name likely emotions. "
    "Ask at most one gentle follow-up question per turn unless the user asks for more. "
    "Offer practical, small next-step suggestions when appropriate (e.g., a script for a tough talk, "
    "a grounding exercise, or a boundary statement), but keep it concise. "
    "If the topic involves a couple (especially a husband and wife), listen from TWO perspectives in a "
    "balanced way: (1) the husband's perspective and (2) the wife's perspective. Validate both sides "
    "without taking sides, and look for the underlying needs on each side. If roles/details are unclear, "
    "ask a clarifying question before assuming. "
    "If you don't know something, say you don't know and do not make up facts. "
    "Safety: If the user expresses intent to self-harm or harm others, encourage them to seek immediate "
    "help (local emergency services or a trusted person) and to reach out right now."
)


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _load_chat_store(store_path: Path) -> dict:
    if not store_path.exists():
        return {"sessions": {}}
    try:
        return json.loads(store_path.read_text(encoding="utf-8"))
    except Exception:
        # If the file is corrupt, don't crash the app.
        return {"sessions": {}}


def _save_chat_store(store_path: Path, store: dict) -> None:
    store_path.parent.mkdir(parents=True, exist_ok=True)
    store_path.write_text(json.dumps(store, ensure_ascii=False, indent=2), encoding="utf-8")


def _sanitize_assistant_output(text: str) -> str:
    # Defensive: user asked that outputs never include <Human> responses.
    if not text:
        return ""
    lines: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("<Human>") or stripped.startswith("Human:"):
            continue
        lines.append(line)
    return "\n".join(lines).strip()


def _choose_or_create_session(store: dict, system_prompt: str) -> tuple[str, list[dict[str, str]]]:
    sessions: dict = store.setdefault("sessions", {})

    existing = list(sessions.items())
    existing.sort(key=lambda kv: kv[1].get("updated_at", ""), reverse=True)

    if existing:
        print("\nSaved chats:")
        for idx, (_sid, meta) in enumerate(existing, start=1):
            name = meta.get("name") or "(unnamed)"
            updated_at = meta.get("updated_at") or "(unknown time)"
            print(f"  {idx}. {name}  —  last used: {updated_at}")

        print("\nChoose an option:")
        print("  [number] Resume that chat")
        print("  n        New chat")

        choice = input("> ").strip().lower()
        if choice and choice != "n" and choice.isdigit():
            pick = int(choice)
            if 1 <= pick <= len(existing):
                session_id = existing[pick - 1][0]
                meta = sessions.get(session_id, {})
                messages = meta.get("messages") or []
                # Ensure the first message is a system prompt.
                if not messages or messages[0].get("role") != "system":
                    messages = [{"role": "system", "content": system_prompt}] + list(messages)
                return session_id, messages

    # New chat
    name = input("Name this chat (optional): ").strip()
    session_id = str(uuid.uuid4())
    messages = [{"role": "system", "content": system_prompt}]
    sessions[session_id] = {
        "name": name or "New chat",
        "created_at": _utc_now_iso(),
        "updated_at": _utc_now_iso(),
        "messages": messages,
    }
    return session_id, messages


def main() -> None:
    api_key = "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"
    if not api_key:
        print(
            "Missing OPENAI_API_KEY.\n"
            "PowerShell example:\n"
            "  $env:OPENAI_API_KEY='your-key-here'\n"
            "Then run:\n"
            "  python test.py"
        )
        return

    model = os.getenv("OPENAI_MODEL", "gpt-5.2")
    system_prompt = os.getenv("SYSTEM_PROMPT", DEFAULT_SYSTEM_PROMPT)

    store_path = Path(__file__).with_name("chat_store.json")
    store = _load_chat_store(store_path)
    session_id, messages = _choose_or_create_session(store, system_prompt)

    client = OpenAI(api_key=api_key)

    def persist() -> None:
        sessions = store.setdefault("sessions", {})
        meta = sessions.setdefault(session_id, {})
        meta["messages"] = messages
        meta["updated_at"] = _utc_now_iso()
        meta.setdefault("created_at", _utc_now_iso())
        meta.setdefault("name", "New chat")
        _save_chat_store(store_path, store)

    persist()
    print("\nChat started.")
    print("Commands: 'exit' to quit, '/reset' to clear this chat.")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye.")
            break

        if not user_input:
            continue

        lowered = user_input.lower()
        if lowered in {"exit", "quit", "/exit", "/quit"}:
            print("Bye.")
            persist()
            break
        if lowered in {"/reset", "reset"}:
            messages = messages[:1]
            print("Conversation reset.")
            persist()
            continue

        messages.append({"role": "user", "content": user_input})

        try:
            response = client.responses.create(
                model=model,
                input=messages,
            )
            answer = _sanitize_assistant_output((response.output_text or "").strip())
        except Exception as e:
            # Remove the last user turn so the conversation state stays consistent.
            messages.pop()
            print(f"Error: {e}")
            continue

        print(f"AI: {answer}")
        messages.append({"role": "assistant", "content": answer})
        persist()


if __name__ == "__main__":
    main()
