def categorize_expense(title):
    title = title.lower()

    if "pizza" in title or "burger" in title or "food" in title:
        return "Food"
    elif "uber" in title or "bus" in title or "train" in title:
        return "Travel"
    elif "electricity" in title or "bill" in title:
        return "Bills"
    elif "shopping" in title or "clothes" in title:
        return "Shopping"
    elif "movie" in title or "netflix" in title or "entertainment" in title:
        return "Entertainment"
    elif "gym" in title or "fitness" in title:
        return "Health"
    elif "gift" in title or "donation" in title:
        return "Gifts"
    elif "salary" in title or "income" in title:
        return "Income"
    elif "rent" in title or "mortgage" in title:
        return "Rent"   
    elif "subscription" in title or "netflix" in title or "spotify" in title:
        return "Subscriptions"
    elif "coffee" in title or "tea" in title:
        return "Beverages"
    elif "phone" in title or "internet" in title:
        return "Utilities"
    elif "book" in title or "course" in title or "education" in title: 
        return "Education"  
    elif "health" in title or "medicine" in title or "doctor" in title:
        return "Healthcare"
    elif "laptop" in title or "gadget" in title or "electronics" in title:
        return "Electronics"
    else:
        return "Other"