import os

def create_folder_structure(base_dir, folder_structure):
    try:
       
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)

        
        for folder_name, subfolders in folder_structure.items():
            folder_path = os.path.join(base_dir, folder_name)
            
           
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                print(f"Folder '{folder_name}' created successfully.")
            else:
                print(f"Folder '{folder_name}' already exists.")
            
           
            if subfolders:
                create_folder_structure(folder_path, subfolders)

    except Exception as e:
        print(f"An error occurred: {e}")


base_directory = "JavaScript_Topics"


folder_structure = {
    "Basics": {
        "Variables and Data Types": None,
        "Operators": None,
        "Conditionals (if-else statements)": None,
        "Loops (for, while loops)": None,
        "Functions (declaration, parameters, return values)": None,
        "Arrays": None,
        "Objects (including JSON)": None,
        "DOM Manipulation (selecting elements, changing content, adding event listeners)": None
    },
    "Intermediate": {
        "Scope and Hoisting": None,
        "Closures": None,
        "Prototypes and Inheritance": None,
        "Error Handling (try-catch)": None,
        "Asynchronous JavaScript (callbacks, promises, async/await)": None,
        "Event Handling": None,
        "Regular Expressions": None,
        "Modules (CommonJS, ES6 Modules)": None
    },
    "Advanced": {
        "Functional Programming (higher-order functions, map, reduce, filter)": None,
        "ES6 Features (arrow functions, template literals, destructuring, spread/rest operators)": None,
        "Memory Management (garbage collection)": None,
        "Promises (chaining, error handling)": None,
        "Generators and Iterators": None,
        "Web APIs (fetch API, localStorage, sessionStorage)": None,
        "WebSockets": None,
        "Browser Rendering and Performance Optimization": None
    },
    "Expert": {
        "Design Patterns (Singleton, Factory, Observer, etc.)": None,
        "Web Workers": None,
        "Service Workers": None,
        "Internationalization and Localization (i18n, l10n)": None,
        "Security (Cross-Site Scripting, Cross-Site Request Forgery, Content Security Policy)": None,
        "Testing (Unit Testing, Integration Testing, End-to-End Testing)": None,
        "Debugging and Profiling": None,
        "Performance Optimization (code splitting, lazy loading, caching)": None
    },
    "Cutting-Edge": {
        "WebAssembly": None,
        "Progressive Web Apps (PWA)": None,
        "Server-Side JavaScript (Node.js)": None,
        "Machine Learning with TensorFlow.js": None,
        "Augmented Reality and Virtual Reality (AR/VR)": None,
        "Blockchain Development with Ethereum": None
    }
}


create_folder_structure(base_directory, folder_structure)
