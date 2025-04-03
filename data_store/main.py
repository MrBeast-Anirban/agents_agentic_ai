from crew import DataStorageCrew

def main():
    crew = DataStorageCrew()
    
    # Anyhow Fetch user data and store for future reference as dictionary 
    print("Storing sample data...")
    result = crew.store_data({
        "name": "Anirban Maitra",
        "email": "m23csa005@iitj.ac.in",
        "age": 10
    })
    print(result)
    
    print("\nSearching for data...")
    search_result = crew.search_data({"name": "Anirban Maitra"})
    print("Search results:", search_result)

    # Use if you want to cleasr the entire json file
    print("\nClearing storage...")
    print(crew.clear_storage())
    
    # Verify if the clear_storage method worked
    print("\nSearching after clear...")
    print(crew.search_data({}))


if __name__ == "__main__":
    main()