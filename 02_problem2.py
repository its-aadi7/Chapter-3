letter = '''Dear <|Name|>
            You are selected!
            <|Date|>'''

print(letter.replace("<|Name|>", "Aadi").replace("<|Date|>", "7 January 2025"))