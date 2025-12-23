import sys

def main():
    print("Checking installed translator packages...\n")

    packages = ['nodes', 'tom', 'edges', 'kg']

    for pkg in packages:
        try:
            # Dynamic import
            module = __import__(f"translator.{pkg}", fromlist=[pkg])
            print(f"✅ [SUCCESS] Imported translator.{pkg}")
            if hasattr(module, 'info'):
                print(f"   Info: {module.info()}")
        except ImportError as e:
            print(f"❌ [MISSING] Could not import translator.{pkg}")
            print(f"   Hint: Try 'pip install -e translator_{pkg}'")
        except Exception as e:
            print(f"⚠️ [ERROR] Error importing translator.{pkg}: {e}")
        print("-" * 30)

if __name__ == "__main__":
    main()
