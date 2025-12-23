# Translator SDK Monorepo Demo

This repository demonstrates a monorepo structure for multiple Python packages sharing a common `translator` namespace.

## Project Structure

The project is organized as a monorepo where each package resides in its own directory.

```
.
├── translator_nodes/       # Package: translator_nodes -> translator.nodes
├── translator_tom/         # Package: translator_tom   -> translator.tom
├── translator_edges/       # Package: translator_edges -> translator.edges
├── translator_kg/          # Package: translator_kg    -> translator.kg
└── translator_sdk/         # Meta-package: translator_sdk
```

## Namespace Packages

All sub-packages share the `translator` top-level namespace. This allows them to be installed and imported independently while appearing as a single unified library to the user.

We use **implicit namespace packages** (PEP 420), which means there is no `__init__.py` in the top-level `translator` directory of each package.

## External Package Hosting

**Yes, sub-packages can be hosted and developed completely independently outside of this monorepo.**

Because we are using namespace packages, Python does not care if the packages come from the same repository or different ones, as long as they are installed in the same environment.

### How to move a package to a separate repository:

1.  **Move the folder**: Simply move the package folder (e.g., `translator_nodes`) to a new git repository.
2.  **Maintain Structure**: Ensure the internal directory structure remains `translator/nodes/...`.
3.  **Install**: Users can install it alongside the other packages.

**Example Scenario:**
*   `translator_tom` is in a separate GitHub repo: `github.com/user/translator-tom`
*   `translator_nodes` is in this monorepo.

You can install both:
```bash
# Install from local monorepo
pip install -e ./translator_nodes

# Install from remote separate repo
pip install git+https://github.com/user/translator-tom.git
```

They will still merge seamlessly under the `translator` namespace:
```python
import translator.nodes
import translator.tom  # Works perfectly!
```

## Development & Installation

### 1. Individual Package Development

You can develop and install each package independently. For local development, use editable installs:

```bash
# Install translator_nodes
pip install -e translator_nodes

# Install translator_tom
pip install -e translator_tom
```

### 2. Using the Packages

Once installed, you can import them under the `translator` namespace:

```python
from translator import nodes
from translator import tom

print(nodes.info())
print(tom.info())
```

### 3. Translator SDK (Meta Package)

The `translator_sdk` is a meta-package that orchestrates the installation of sub-packages.

**Note:** Since these packages are not published to PyPI, installing `translator_sdk` directly will fail to find the dependencies. In a real-world scenario, you would publish `translator_nodes`, `translator_tom`, etc., to a package index (PyPI or private), and then `translator_sdk` would resolve them.

For local development of the SDK concept, you can install the sub-packages manually as shown above.

If published, you could install the SDK with specific components:

```bash
# Install everything
pip install "translator_sdk[all]"

# Install specific components
pip install "translator_sdk[nodes,kg]"
```

## Demo Script

Assuming you have installed the packages (e.g., via `pip install -e translator_nodes -e translator_tom ...`), you can run the following python code:

```python
try:
    from translator import nodes
    print(f"Nodes: {nodes.info()}")
except ImportError:
    print("translator.nodes not installed")

try:
    from translator import tom
    print(f"TOM: {tom.info()}")
except ImportError:
    print("translator.tom not installed")

try:
    from translator import edges
    print(f"Edges: {edges.info()}")
except ImportError:
    print("translator.edges not installed")

try:
    from translator import kg
    print(f"KG: {kg.info()}")
except ImportError:
    print("translator.kg not installed")
```
