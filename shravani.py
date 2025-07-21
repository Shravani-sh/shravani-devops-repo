name = input("What is your name? ")

print("🚨 SYSTEM ALERT 🚨")
print(f"Hi {name}... We've been expecting you.")
print("Analyzing your awesomeness level...")
print("🧠 Beep boop... Processing...")

awesome = len(name) * 42  # Totally scientific formula

print(f"✨ Results: Your awesomeness score is {awesome}!")
if awesome > 200:
    print("⚡ You're too awesome. We must shut down the system to avoid jealousy.")
else:
    print("😎 Just the right amount of coolness. Proceed, human.")
