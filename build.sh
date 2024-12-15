#!/bin/bash

# Generate an index for projects
echo "# Projects Portfolio" > projects/README.md
echo "" >> projects/README.md
echo "## Projects" >> projects/README.md
echo "" >> projects/README.md

for project in ./projects/*; do
    if [ -d "$project" ]; then
        project_name=$(basename "$project")
        echo "Processing $project_name"
        readme_path="./projects/$project_name/README.md"
        if [ -f "$readme_path" ]; then
            description=$(head -n 1 "$readme_path")
            echo "- [$project_name](./$project_name/README.md): $description" >> projects/README.md
        else
            echo "- $project_name: No description available" >> projects/README.md
        fi
    fi
done

echo "Projects index generated."
