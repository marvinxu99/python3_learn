import textwrap

websiteText = """     Learning an happend any where with our apps on your computer, mobile devices, and TV, featuring enhanced navigation and faster streaming for
anytime learning. limitless learning, limitless possibilities.
"""
print('**No dedent**')
print(textwrap.fill(websiteText))

print('**Dedent**')
dedent_text = textwrap.dedent(websiteText).strip()
print(dedent_text)

print('**Fill**')
print(textwrap.fill(dedent_text, width=50))
print(textwrap.fill(dedent_text, width=100))

print("**Controlling Indent**")
print(textwrap.fill(dedent_text, initial_indent="    ", subsequent_indent=""))
print(textwrap.fill(dedent_text, initial_indent="    ", subsequent_indent="        "))

print("**Shortening Text**")
short = textwrap.shorten("LinkedIn.com is great!", width=15, placeholder="...")
print(short)

