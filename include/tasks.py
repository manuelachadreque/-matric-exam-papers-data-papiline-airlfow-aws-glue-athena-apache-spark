import requests


subject_links = {
    "Mathematics": "https://s3.af-south-1.amazonaws.com/www.teachme2.com/matric-past-papers/2018-2023-Mathematics.zip",
    "Physical Sciences": "https://s3.af-south-1.amazonaws.com/www.teachme2.com/matric-past-papers/2018-2023-Physical-Sciences.zip",
    "Accounting": "https://s3.af-south-1.amazonaws.com/www.teachme2.com/matric-past-papers/2018-2023-Accounting.zip",
    "English": "https://s3.af-south-1.amazonaws.com/www.teachme2.com/matric-past-papers/2018-2023-English.zip"
}

def get_file(url):
    try:
        response = requests.get(url,stream=True)
        return response
    
    except requests.exceptions.RequestException as e:
        print(f"Error getting file {url}  : {e}")
        return None
    

