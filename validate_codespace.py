#!/usr/bin/env python3
"""
Codespace validation script for TradingAgents
This script validates that the codespace environment is set up correctly.
"""

import sys
import os
from pathlib import Path

def check_python_version():
    """Check if Python version meets requirements."""
    version = sys.version_info
    required_major, required_minor = 3, 10
    
    if version.major < required_major or (version.major == required_major and version.minor < required_minor):
        print(f"❌ Python {required_major}.{required_minor}+ required, found {version.major}.{version.minor}")
        return False
    else:
        print(f"✅ Python version: {version.major}.{version.minor}.{version.micro}")
        return True

def check_environment_variables():
    """Check if required environment variables are configured."""
    required_vars = ["FINNHUB_API_KEY", "OPENAI_API_KEY"]
    optional_vars = ["ANTHROPIC_API_KEY", "GOOGLE_API_KEY"]
    
    all_configured = True
    
    print("\n🔧 Environment Variables:")
    for var in required_vars:
        if os.getenv(var):
            print(f"✅ {var}: configured")
        else:
            print(f"❌ {var}: not configured (required)")
            all_configured = False
    
    for var in optional_vars:
        if os.getenv(var):
            print(f"✅ {var}: configured (optional)")
        else:
            print(f"⚠️  {var}: not configured (optional)")
    
    return all_configured

def check_project_structure():
    """Check if project structure is correct."""
    required_paths = [
        "tradingagents",
        "cli",
        "README.md",
        "pyproject.toml",
        "requirements.txt"
    ]
    
    print("\n📁 Project Structure:")
    all_exist = True
    
    for path in required_paths:
        if Path(path).exists():
            print(f"✅ {path}: found")
        else:
            print(f"❌ {path}: missing")
            all_exist = False
    
    return all_exist

def check_imports():
    """Check if basic imports work."""
    print("\n📦 Import Tests:")
    
    try:
        sys.path.insert(0, '.')
        import tradingagents
        print("✅ tradingagents: importable")
        return True
    except ImportError as e:
        print(f"❌ tradingagents: import failed - {e}")
        return False

def main():
    """Run all validation checks."""
    print("🚀 TradingAgents Codespace Validation")
    print("=" * 50)
    
    checks = [
        ("Python Version", check_python_version),
        ("Environment Variables", check_environment_variables),
        ("Project Structure", check_project_structure),
        ("Basic Imports", check_imports),
    ]
    
    results = []
    for check_name, check_func in checks:
        try:
            result = check_func()
            results.append(result)
        except Exception as e:
            print(f"❌ {check_name}: failed with error - {e}")
            results.append(False)
    
    print("\n" + "=" * 50)
    print("📊 Summary:")
    
    if all(results):
        print("🎉 All checks passed! Your codespace is ready to use.")
        print("\n🔧 Next steps:")
        print("1. Configure your API keys in .env file")
        print("2. Run: python main.py (to test the main script)")
        print("3. Run: python -m cli.main analyze (to test the CLI)")
        return 0
    else:
        print("⚠️  Some checks failed. Please review the issues above.")
        print("\n💡 Common solutions:")
        print("- Make sure you're in the correct directory")
        print("- Copy .env.example to .env and configure your API keys")
        print("- Run: pip install -e . to install the package")
        return 1

if __name__ == "__main__":
    sys.exit(main())