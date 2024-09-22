import yaml
import graphviz


def extract_task_names(file_path):
    """
    Extracts task names from a YAML file.

    Args:
        file_path (str): Path to the YAML file.

    Returns:
        list: List of task names if found, otherwise None.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)

            # List to store task names
            task_names = []

            # Recursive function to find all 'name' entries in the YAML
            def find_names(data):
                if isinstance(data, dict):
                    if "name" in data:
                        task_names.append(data["name"])
                    for _, value in data.items():
                        find_names(value)
                elif isinstance(data, list):
                    for item in data:
                        find_names(item)

            # Start searching for 'name' keys
            find_names(yaml_data)

            # Check if any names were found
            if task_names:
                return task_names
            print("No task names were found in the YAML file.")
            return None

    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None


def generate_diagram(task_names):
    """
    Generates a diagram from the extracted task names and saves it as a .png file using Graphviz.

    Args:
        task_names (list): List of task names to be used in the diagram.
    """
    if not task_names:
        print("No task names provided to generate the diagram.")
        return

    # Create a new directed graph using graphviz
    dot = graphviz.Digraph(comment="Task Diagram")

    # Add nodes for each task name, ensuring only strings are used
    for i, name in enumerate(task_names, 1):
        if isinstance(name, list):
            # Convert list to string if it's a list
            name = ", ".join(map(str, name))
        if isinstance(name, str):
            dot.node(str(i), name)
        else:
            print(f"Skipping invalid task name: {name}")

    # Optionally, you could add some edges (for example, in sequential order)
    for i in range(1, len(task_names)):
        dot.edge(str(i), str(i + 1))

    # Save the diagram to a file without specifying the .png extension
    diagram_path = "task_diagram"  # No .png here
    dot.render(diagram_path, format="png", cleanup=True)
    print(f"Diagram saved as {diagram_path}.png")


if __name__ == "__main__":
    # Path to your role's main.yml file
    file_path = "ansible/roles/restore/tasks/main.yml"
    task_names = extract_task_names(file_path)

    if task_names:
        generate_diagram(task_names)
    else:
        print("No tasks were found in the YAML file.")


"""
autopep8 --in-place --aggressive --aggressive generate_diagram.py
black generate_diagram.py
pylint generate_diagram.py
"""
