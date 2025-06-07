from src.predict import predict

def main():
    print("Welcome to LangSnap - Language Identifier CLI")
    while True:
        text = input("\nEnter text (or 'exit' to quit): ").strip()
        if text.lower() == 'exit':
            print("Goodbye!")
            break
        language, confidence = predict(text)
        print(f"Predicted Language: {language} ({confidence:.2f}% confidence)")

if __name__ == "__main__":
    main()
