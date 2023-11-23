
#!/bin/bash



# Find and delete files not ending in '.cpp' or '.py'
find . -type f \( -name "*.o" -o ! -name "*.*" \) -delete

# Print a message
echo "Files deleted successfully."
