import requests

class Super_hiro:

    def list_with_object(self):
        global_list = list()
        for i in range(0,3,1):
            if i == 0:
                name = "Hulk"
            if i == 1:
                name = "Thanos"
            if i == 2:
                name = "Captain America"
            response = requests.get(f"https://superheroapi.com/api/2619421814940190/search/{name}")
            print(response.json())
            global_list.append(response.json())
        return global_list

    def super_intelligence(self, gl):
        global_list = gl
        super_dict = dict()
        for element in global_list:
            #print(element['results-for'])
            for elem in element["results"]:
                print(elem["name"])
                print(elem["powerstats"]["intelligence"])
                intelligence = elem["powerstats"]["intelligence"]
                super_dict[elem["name"]] = f"intelligence: {intelligence}"

        return super_dict

Superhiro = Super_hiro()
print(Superhiro.super_intelligence(Superhiro.list_with_object()))
