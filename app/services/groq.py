import os
import httpx

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

async def generate_persona_text(educational_background: str, family_background: str) -> str:
    prompt = (
        f"Given this educational background: {educational_background} "
        f"and this family background: {family_background}, generate a concise persona "
        f"in 2-3 paragraphs discussing likely personality traits, interests, and career inclinations."
    )
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={"Authorization": f"Bearer {GROQ_API_KEY}"},
                json={
                    "model": "llama3-8b-8192",
                    "messages": [{"role": "user", "content": prompt}]
                },
                timeout=15
            )
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        raise RuntimeError(f"Groq API error: {e}")
