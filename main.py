import pandas as pd
import matplotlib.pyplot as plt
import nltk
from bs4 import BeautifulSoup
import requests


class DataScraper:
    @staticmethod
    def scrape_data(url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            data = soup.find_all('div', class_='data')
            return data
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while scraping data: {e}")
            return []


class DataPreprocessor:
    @staticmethod
    def preprocess_data(data):
        cleaned_data = [item.text.strip() for item in data]
        return cleaned_data


class DataAnalyzer:
    @staticmethod
    def analyze_data(data):
        df = pd.DataFrame(data, columns=['Data'])
        df['Length'] = df['Data'].str.len()
        mean_length = df['Length'].mean()
        max_length = df['Length'].max()
        analysis_results = {
            'mean_length': mean_length,
            'max_length': max_length
        }
        return analysis_results


class DataVisualizer:
    @staticmethod
    def create_visualizations(data):
        df = pd.DataFrame(data, columns=['Data'])
        df['Length'] = df['Data'].str.len()
        plt.hist(df['Length'], bins=20)
        plt.xlabel('Length')
        plt.ylabel('Frequency')
        plt.title('Distribution of Data Length')
        plt.show()


class NLPProcessor:
    @staticmethod
    def perform_nlp(data):
        tokenized_data = [nltk.word_tokenize(item) for item in data]
        return tokenized_data


class DataUpdater:
    @staticmethod
    def update_data(url):
        try:
            updated_data = DataScraper.scrape_data(url)
            return updated_data
        except Exception as e:
            print(f"An error occurred while updating data: {e}")
            return []


class DataExporter:
    @staticmethod
    def export_data(data, export_format):
        if export_format == 'csv':
            df = pd.DataFrame(data, columns=['Data'])
            df.to_csv('data.csv', index=False)
        elif export_format == 'json':
            df = pd.DataFrame(data, columns=['Data'])
            df.to_json('data.json', orient='records')
        else:
            print("Invalid export format. Please choose either 'csv' or 'json'.")


class UserInterface:
    @staticmethod
    def main_menu():
        print('1. Scrape data')
        print('2. Preprocess data')
        print('3. Analyze data')
        print('4. Create visualizations')
        print('5. Perform NLP tasks')
        print('6. Update data')
        print('7. Export data')
        print('0. Exit')

    @staticmethod
    def user_interface():
        data = []
        processed_data = []

        while True:
            UserInterface.main_menu()
            choice = input('Enter your choice: ')

            if choice == '1':
                url = input('Enter the URL to scrape data from: ')
                data = DataScraper.scrape_data(url)
                if data:
                    print('Data scraped successfully!')
                    print(data)

            elif choice == '2':
                if not data:
                    print('No data available. Please scrape data first.')
                    continue
                processed_data = DataPreprocessor.preprocess_data(data)
                if processed_data:
                    print('Data preprocessed successfully!')
                    print(processed_data)

            elif choice == '3':
                if not processed_data:
                    print(
                        'No preprocessed data available. Please preprocess data first.')
                    continue
                analysis_results = DataAnalyzer.analyze_data(processed_data)
                print('Data analysis completed successfully!')
                print(analysis_results)

            elif choice == '4':
                if not processed_data:
                    print(
                        'No preprocessed data available. Please preprocess data first.')
                    continue
                DataVisualizer.create_visualizations(processed_data)

            elif choice == '5':
                if not data:
                    print('No data available. Please scrape data first.')
                    continue
                tokenized_data = NLPProcessor.perform_nlp(data)
                if tokenized_data:
                    print('NLP tasks performed successfully!')
                    print(tokenized_data)

            elif choice == '6':
                url = input('Enter the URL to update data from: ')
                updated_data = DataUpdater.update_data(url)
                if updated_data:
                    data = updated_data
                    print('Data updated successfully!')
                    print(data)

            elif choice == '7':
                if not processed_data:
                    print(
                        'No preprocessed data available. Please preprocess data first.')
                    continue
                export_format = input('Enter the export format (csv/json): ')
                DataExporter.export_data(processed_data, export_format)
                print('Data exported successfully!')

            elif choice == '0':
                break

            else:
                print('Invalid choice.')


# Execution
if __name__ == "__main__":
    UserInterface.user_interface()
