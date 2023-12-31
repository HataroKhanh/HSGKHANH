import pandas as pd

f = {
    "name": ["Alice", "Bob", "Charlie"],
    "img": ["image1.jpg", "image2.jpg", "image3.jpg"]
}

# Create a DataFrame
df = pd.DataFrame(f)

# Export to Excel
df.to_excel("output.xlsx", index=False)
