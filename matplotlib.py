import pandas as pd
import matplotlib.pyplot as plt

# Creating a DataFrame from the provided data
data = {
    'Name': ['Drake', 'Post Malone', 'Ed Sheeran', 'J Balvin', 'Bad Bunny', 'Justin Bieber', 'Ozuna', 'Ariana Grande', 'Khalid', 'Daddy Yankee'],
    'ID': ['3TVXtAsR1Inumwj472S9r4', '246dkjvS1zLTtiykXe5h60', '6eUKZXaKkcviH0Ku9w2n3V', '1vyhD5VmyZ7KMfW5gqLgo5', '4q3ewBCX7sLwd24euuV69X',
           '1uNFoZAHBGtllmzznpCI3s', '1i8SpTcr7yvPOmcqrbnVXY', '66CXWjxzNUsdJxJ2JdwvnR', '6LuN9FCkKOj5PcnpouEgny', '4VMYDCV2IEDYJArk749S6m'],
    'Gender': ['male', 'male', 'male', 'male', 'male', 'male', 'male', 'female', 'male', 'male'],
    'Age': [33, 25, 29, 35, 26, 26, 28, 27, 22, 43],
    'Country': ['CA', 'US', 'GB', 'CO', 'PR', 'CA', 'PR', 'US', 'US', 'PR'],
    'Genres': [['canadian hip hop', 'canadian pop', 'hip hop', 'pop rap', 'rap'],
               ['dfw rap', 'melodic rap', 'pop', 'rap'],
               ['pop', 'singer-songwriter pop', 'uk pop'],
               ['reggaeton', 'reggaeton colombiano', 'trap latino', 'urbano latino'],
               ['reggaeton', 'trap latino', 'urbano latino'],
               ['canadian pop', 'pop'],
               ['puerto rican pop', 'reggaeton', 'trap latino', 'urbano latino'],
               ['pop'],
               ['pop', 'pop r&b'],
               ['latin hip hop', 'reggaeton', 'trap latino', 'urbano latino']],
    'Popularity': [95, 86, 87, 83, 95, 88, 84, 88, 81, 84],
    'Followers': [83298497, 43130108, 115998928, 38028010, 77931484, 75112165, 38192380, 95710972, 16282583, 34243502],
    'URI': ['spotify:artist:3TVXtAsR1Inumwj472S9r4', 'spotify:artist:246dkjvS1zLTtiykXe5h60', 'spotify:artist:6eUKZXaKkcviH0Ku9w2n3V',
            'spotify:artist:1vyhD5VmyZ7KMfW5gqLgo5', 'spotify:artist:4q3ewBCX7sLwd24euuV69X', 'spotify:artist:1uNFoZAHBGtllmzznpCI3s',
            'spotify:artist:1i8SpTcr7yvPOmcqrbnVXY', 'spotify:artist:66CXWjxzNUsdJxJ2JdwvnR', 'spotify:artist:6LuN9FCkKOj5PcnpouEgny',
            'spotify:artist:4VMYDCV2IEDYJArk749S6m']
}

df = pd.DataFrame(data)

# Displaying basic information about the DataFrame
print("Basic Information about the DataFrame:")
print(df.info())

# Displaying the first few rows of the DataFrame
print("\nFirst few rows of the DataFrame:")
print(df.head())

# Creating a bar graph for the top artists based on popularity
plt.figure(figsize=(10, 6))
plt.bar(df['Name'], df['Popularity'], color='skyblue')
plt.title('Popularity of Top Artists')
plt.xlabel('Artist Name')
plt.ylabel('Popularity')
plt.xticks(rotation=45, ha='right')
plt.show()

