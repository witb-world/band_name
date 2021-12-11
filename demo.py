import discogs_client
import sys
import os

def get_access_token():
  token = os.environ.get('DISCOGS_ACCESS_TOKEN')
  return token

def name_input():
  search_name_query = sys.argv[1]
  return search_name_query

def parse_results(query, results):
  for result in results:
    name = result.name
    name = name.split(" (")[0]
    if query.lower() == name.lower() or ("the " + query).lower() == (name).lower():
      print(name)

def run_search():
  d = discogs_client.Client('DemoApp/0.1.2', user_token=get_access_token())

  search_name_query = name_input()
  results = d.search(search_name_query, type='artist')

  parse_results(search_name_query, results)

def main():
  run_search()

if __name__ == "__main__":
  main()
