import json
import os



# gigs website development (7)
# Filter gigs website development (7)

input_directory = 'gigs website development (7)'
output_directory = 'Filter gigs website development (7)'


# Create the output directory if it does not exist
os.makedirs(output_directory, exist_ok=True)


def get_choice_type(gig):
    choice_eligibilities = gig.get("choice_eligibilities", None)
    
    # Case 1: choice_eligibilities is None
    if choice_eligibilities is None:
        return "NULL"
    
    # Case 2: choice_eligibilities is an empty list
    if isinstance(choice_eligibilities, list) and not choice_eligibilities:
        return "EMPTY"
    
    # Case 3 and 4: choice_eligibilities is a list with items
    if isinstance(choice_eligibilities, list):
        types = [eligibility.get("type") for eligibility in choice_eligibilities if "type" in eligibility]
        
        # Case 3: Single item (e.g., ALGO_A)
        if len(types) == 1:
            return types[0]
        
        # Case 4: Multiple items, join them with "&" (e.g., ALGO_A&B)
        return "&".join(sorted(types))  # Sorting ensures a consistent order
    
    return None  # Default case if something unexpected is encountered



# Iterate over all JSON files in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith('.json'):
        input_path = os.path.join(input_directory, filename)
        
        try:
            # Open the file with UTF-8 encoding
            with open(input_path, 'r', encoding='utf-8') as file: 
                data = json.load(file)
            
            # Extract the relevant information
            filtered_listings = []
            listing = data.get('reviews')
            if listing.get('reviews', []):
                    for review in listing.get('reviews', []):
                        # choice = get_choice_type(gig)


                        filtered_gig = {

                            "memberSince": data['sellerCard']['memberSince'],
                            "responseTime": data['sellerCard']['responseTime'],
                            "recentDelivery": data['sellerCard']['recentDelivery'],
                            "title": data['overview']['gig']['title'],
                            "rating": data['overview']['gig']['rating'],
                            "ordersInQueue": data['overview']['gig']['ordersInQueue'],
                            "repeatScore": data['repeatScore']['score'],

                            
                            
                            "order_duration_in_days": review.get("order_duration_in_days"),
                            "order_price_range_usd": review.get("order_price_range_usd"),
                            # "type": review.get("type", "normal"),           #promoted_gig
                            "comment": review.get("comment"),
                            "reviewer_country_code": review.get("reviewer_country_code"),
                            "created_at": review.get("created_at"),
                            "value": review.get("value"),
                            "score": review.get("score"),
                            "repeat_buyer": review.get("repeat_buyer"),
                            "is_business": review.get("is_business"),
                            "gig_id": review.get("gig_id"),
                            "relevancy_score": review.get("relevancy_score"),
                            "reviews_count_as_buyer": review.get("reviews_count_as_buyer"),
                            "is_cancelled_order": review.get("is_cancelled_order"),
                            "is_business": review.get("is_business"),
                            "score": review.get("score"),
                            # "choice_eligibilities": choice,
                            # "listingQuery": data['listingQuery']


                        }
                        filtered_listings.append(filtered_gig)
                # if listing.get('roles', []):
                #     for gig in listing.get('roles', []):
                #         filtered_gig = {
                #             "timestamp": data['tracking']['reportData']['page']['timestamp'],
                #             # "gigId": gig.get("gigId"),
                #             "pos": gig.get("position"),
                #             "is_fiverr_choice": False,

                #             "seller_name": gig.get("seller", {}).get("username"),
                #             "seller_country": gig.get("seller", {}).get("countryCode"),
                #             "seller_level": gig.get("seller", {}).get("level"),

                #             "is_pro": gig.get("role", {}).get("isPro"),
                #             "buying_review_rating_count": gig.get("role", {}).get("ordersAmount"),
                #             "buying_review_rating": gig.get("role", {}).get("review", {}).get("score"),
                #             "price_i": gig.get("role", {}).get("minPrice"),                            
                #             "count": gig.get("role", {}).get("review", {}).get("count"),
                #             "score": gig.get("role", {}).get("review", {}).get("score")
                #         }
                #         filtered_listings.append(filtered_gig)                    


            
            # Create a new JSON file with the filtered data
            filtered_data = {
                "listings": filtered_listings
            }
            
            output_path = os.path.join(output_directory, filename)
            with open(output_path, 'w', encoding='utf-8') as file:
                json.dump(filtered_data, file, indent=4)
            
            print(f"Filtered JSON file '{filename}' has been created successfully.")
        
        except UnicodeDecodeError as e:
            print(f"Error decoding file '{filename}': {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON in file '{filename}': {e}")
        except Exception as e:
            print(f"An unexpected error occurred with file '{filename}': {e}")

print("All JSON files have been processed.")


