
class League:
    def __init__(self, data):  
        self.league_id = data['league_id']
        self.name = data['name']
        self.nation = data['nation']
        self.league_level = data['league_level']
        self.n_teams = data['squad_size']
        self.logo = data['logo']
        self.transfermarkt_id = data['transfermarkt_id']
        self.diretta_id = data['diretta_id']
        self.fbref_id = data['fbref_id']
        self.get_transfermarkt_url = data['get_transfermarkt_url']
        self.get_direttait_url = data['get_direttait_url']
        self.get_fbref_url = data['get_fbref_url']  
        
    def to_dict(self):
        return {
            'league_id': self.league_id,
            'name': self.name,
            'nation': self.nation,
            'league_level': self.league_level,
            'n_teams': self.n_teams,
            'logo': self.logo,
            'transfermarkt_id': self.transfermarkt_id,
            'transfermarkt_url': self.get_transfermarkt_url(),
            'diretta_id': self.diretta_id,
            'diretta_url': self.get_direttait_url(),
            'fbref_id': self.fbref_id,
            'fbref_url': self.get_fbref_url()
        }
