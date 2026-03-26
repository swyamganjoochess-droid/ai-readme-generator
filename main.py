def generate_readme(name, desc):
    return f"# {name}\n\n## Description\n{desc}"

name = input("Project name: ")
desc = input("Description: ")

output = generate_readme(name, desc)

with open("README_generated.md", "w") as f:
    f.write(output)

print("Done!")
