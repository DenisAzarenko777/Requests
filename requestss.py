import requests

class Super_hiro:
    def list_with_object2(self,super_list):
        global_list = list()
        self.super_list = super_list
        for element in super_list:
            response = requests.get(f"https://superheroapi.com/api/2619421814940190/search/{element}")
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

hero_list_data = ['Hulk', 'Captain', 'America', 'Thanos']
Superhiro = Super_hiro()
print(Superhiro.super_intelligence(Superhiro.list_with_object2(hero_list_data)))




