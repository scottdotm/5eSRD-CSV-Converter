import csv
import requests # type: ignore
import json

# Base URL for the DnD 5e API
base_url = "https://www.dnd5eapi.co"

# Function to scrape data from a URL
def scrape_data(url):
  response = requests.get(url)
  if response.status_code == 200:
    data = json.loads(response.text)
    return data
  else:
    print(f"Error: Failed to fetch data from {url}")
    return None

# Scrape data from the base URL
data = scrape_data(base_url + "/api")

# Specify the categories you want to access (modify as needed)
categories = []

if data:
  # Iterate through each category in the response
  for category, url in data.items():
    # Construct the full URL for the category (fix the typo)
    full_url = f"{base_url}{url}"

    # Scrape data for the specific category
    category_data = scrape_data(full_url)

    if category_data:
      categories.append(url)
      
# Open a CSV file for writing
with open('dnd5e_data.csv', 'w', newline='') as csvfile:
  # Create a CSV writer object
  writer = csv.writer(csvfile)

  for category in categories:
      full_url = f"{base_url}{category}"
      category_data = scrape_data(full_url)

      if category_data:
          print(category_data)
          if "results" in category_data:
              # Write the category count
              writer.writerow([category_data["count"]])
              writer.writerow(['!' * 200])  # Separator line
              myjson = []
              columns = ["Index", "Name", "URL", "Description", "Skills", "Abbrevisation", "Starting Proficiencies", "Language Options", "Starting Equipment", "Starting Equipment Options", "Typical Speakers", "Script", "Type of Proficiency", "Classes", "Races", "Reference", "Hit Dice", "Class Levels", "Multiclassing", "Prerequisites", "Minimum Score", "Prerequisite Options" , "Choose This Many", "From This Thing",  "Proficiencies", "Spellcasting", "Level", "Information", "Spellcasting Abiility", "Spells", "Saving Throws", "Subclasses", "Cantrips", "Spells Known", "Spell Slot 1", "Spell Slot 2", "Spell Slot 3","Spell Slot 4","Spell Slot 5","Spell Slot 6","Spell Slot 7", "Spell Slot 8", "Spell Slot 9", "Class Specific", "Equipment", "Image", "Equipment Categories", "Variants", "Variant", "Parent","Feature Specific","Speed", "Ability Bonus", "Bonus", "Alignment", "Age", "Size","Size Description", "Starting Proficiencies", "Starting Proficiency Options", "Language", "Language Description", "Traits", "Higher Level", "Range", "Components", "Material", "Ritual", "Duration", "Concentration", "Casting Time", "Attack Type", "Damage", "School"]
              writer.writerow(columns)
              for result in category_data["results"]:
                  if "url" in result:
                      #print({result['index']}, {result['name']}, {result['url']})
                      full_url = f"{base_url}{result['url']}"
                      data = scrape_data(full_url)
                      myjson.append(data)
                  else:
                      print(f"No URL found for {result['index']}")
              # Filter results with data and write to CSV
              filtered_results = [result for result in category_data["results"] if any(result.values())]
              if filtered_results:
                for response in myjson:
                  row_data = [
                    response.get('index'),
                    response.get('name'),
                    response.get('url'), 
                    response.get('desc', ''),
                    response.get('skills', ''),
                    response.get('abbreviation', ''),
                    response.get('starting_proficiencies', ''),
                    response.get('language_options', ''),
                    response.get('starting_equipment', ''),
                    response.get("starting_equipment_options", ''),
                    response.get("typical_speakers", ''),
                    response.get('script', ''),
                    response.get('type', ''),
                    response.get('classes', ''),
                    response.get('races', ''),
                    response.get('reference',''),
                    response.get('hit_die', ''),
                    response.get('class_levels', ''),
                    response.get('multi_classing', ''),
                    response.get('prerequisites', ''),
                    response.get('minimum_score', ''),
                    response.get('prerequisite_options', ''),
                    response.get('choose', ''),
                    response.get('from', ''),
                    response.get('proficiencies',''),
                    response.get('spellcasting', ''),
                    response.get('level', ''),
                    response.get('info', ''),
                    response.get('spellcasting_ability', ''),
                    response.get('spells', ''),
                    response.get('saving_throws', ''),
                    response.get('subclasses', ''),
                    response.get('cantrips_known', ''),
                    response.get('spells_known', ''),
                    response.get('spell_slots_level_1', ''),
                    response.get('spell_slots_level_2', ''),
                    response.get('spell_slots_level_3', ''),
                    response.get('spell_slots_level_4', ''),
                    response.get('spell_slots_level_5', ''),
                    response.get('spell_slots_level_6', ''),
                    response.get('spell_slots_level_7', ''),
                    response.get('spell_slots_level_8', ''),
                    response.get('spell_slots_level_9', ''),
                    response.get('class_specific', ''),
                    response.get('equipment', ''),
                    response.get('image', ''),
                    response.get("equipment_category", ''),
                    response.get('variants', ''),
                    response.get('variant', ''),
                    response.get('parent', ''),
                    response.get('feature_specific', ''),
                    response.get('speed', ''),
                    response.get('ability_bonuses', ''),
                    response.get('bonus', ''),
                    response.get('alignement', ''),
                    response.get('age', ''),
                    response.get('size', ''),
                    response.get('size_description',''),
                    response.get('starting_proficiencies', ''),
                    response.get('starting_proficiency_options', ''),
                    response.get('languages', ''),
                    response.get('language_desc', ''),
                    response.get('traits', ''),
                    response.get('higher_level', ''),
                    response.get('range', ''),
                    response.get('components', ''),
                    response.get('material', ''),
                    response.get('ritual', ''),
                    response.get('duration', ''),
                    response.get('concentration', ''),
                    response.get('casting_time', ''),
                    response.get('attack_type', ''),
                    response.get('damage',''),
                    response.get('school', '')
                    #response.get('',''),
                  ]
                  writer.writerow(row_data)
                writer.writerow(['!' * 200])  # Separator line
                print(row_data)
          else:
              print(f"No results found for {category}")
print("Data successfully scraped and written to dnd5e_data.csv")