import random
import re

class SimpleAI:
    def __init__(self):
        self.memory = {}  # Stores word associations

    def learn(self, text):
        words = re.findall(r'\b\w+\b', text.lower())
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            if w1 not in self.memory:
                self.memory[w1] = []
            self.memory[w1].append(w2)

    def generate_reply(self, seed_word=None, max_words=15):
        if not self.memory:
            return "I don’t know much yet. Tell me something!"
        
        if not seed_word or seed_word not in self.memory:
            seed_word = random.choice(list(self.memory.keys()))

        reply = [seed_word]
        for _ in range(max_words - 1):
            next_words = self.memory.get(reply[-1])
            if not next_words:
                break
            reply.append(random.choice(next_words))
        return " ".join(reply)

    def chat(self):
        print("🤖 AI: Hello! Let's chat. (type 'exit' to stop)")
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() in {"exit", "quit"}:
                print("🤖 AI: Bye!")
                break

            self.learn(user_input)
            seed = random.choice(re.findall(r'\b\w+\b', user_input.lower())) if user_input else None
            print("🤖 AI:", self.generate_reply(seed))

# Run it
if __name__ == "__main__":
    bot = SimpleAI()
    bot.chat()

