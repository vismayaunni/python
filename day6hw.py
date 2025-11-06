# List of blog post views
blog_views = [150, 800, 2500, 600, 1200, 450, 3000]

# Initialize counters
total_views = 0
trending_count = 0

# Loop through each blog view
for views in blog_views:
    total_views += views  # Add to total views

    if views > 1000:
        print("Trending")
        trending_count += 1
    elif 500 <= views <= 1000:
        print("Average")
    else:
        print("Low Traffic")

# After the loop
print("\nTotal Views:", total_views)
print("Number of Trending Posts:", trending_count)
