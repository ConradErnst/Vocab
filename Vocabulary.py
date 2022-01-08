import docx
import  requests
import json
import python-docx


def vocab_text(n):
    app_id = '131c5c9f'
    app_key = '93c863593eaf2c3b3d04306d37017cae'
    language = 'en-gb'
    for word in n:
        word_id = str(word)
        fields = 'definitions'
        url = 'https://od-api.oxforddictionaries.com/api/v2/entries/'  + language + '/' + word_id.lower() + '?fields=' + fields
        r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})
        return("text \n" + r.text)

vocab_text(['anonymity'])

def vocab_define():
    print(vocab_text()

#['Subsume', 'Anonymity', 'Matriarch', 'Emphatically', 'Grovel', 'Benevolent', 'Odious', 'Conceded', 'Solicitous', 'tenacious ', 'Capriciousness', 'Lynched', 'Frivolous', 'Flummoxed', 'Pejorative', 'Quintessential', 'Enebriated', 'Angulation', 'Impetus', 'Loquacious', 'Ravishing', 'Ravenous', 'Huberous', 'Parity', 'Zeal', 'Frivolity', 'Holistic', 'Circumvent', 'Copious', 'Envisaging', 'Contemporaneous', 'Radical', 'Mitigation', 'Bigotry', 'Infatuated', 'Incandescent', 'Ubiquitous', 'Lethargic', 'Mondain', 'Vivisection', 'Premonition', 'Deduction', 'Console', 'Humility', 'Surrealism', 'Ambivalent', 'Mortality', 'Tantalizing', 'Eerily', 'Articulate', 'Temperament', 'Deception', 'Consecrated', 'Visceral', 'Equanimity', 'Competent', 'Cynic', 'Contrition', 'Obstinate', 'Coquette', 'Vulgar', 'Morose', 'Platitude', 'Pretentious', 'Apathy', 'Precocious', 'Bombastic', 'Eminently', 'Bodacious', 'Incendiary', 'Atrocious', 'Fruition', 'Egress', 'Recuse', 'Assail', 'Jaunty', 'Coronary', 'Minajatwa', 'Libation', 'Wayward', 'Unbecoming', 'Insinuating', 'Purgatory', 'Equestrian', 'Innuendo', 'Neolithic', 'Fortuitous', 'Vacilate', 'Advantageous', 'Imbue', 'Ostensibly', 'Judiciously', 'Evanescent', 'Fetid', 'Capacious', 'Ire', 'Vigilant', 'Perturbation', 'Prescient', 'Regal', 'Subservient', 'Feigned', 'Docile', 'Precluded', 'Misnomer', 'Litany', 'Effete', 'Wanton', 'Surreptitiously', 'Cacophony', 'Brooding', 'Recapitulate', 'Formidable', 'Whinge', 'Ostentatiousness', 'Dilenttante', 'Derogatory', 'Egregiously', 'Anonymity', 'Assiduously', 'Chauvinist', 'Contrive', 'Ascribe', 'Invidious', 'Anomie', 'Dismal', 'Monogamous', 'Ardent', 'Phonetically', 'Moratorium', 'Bowuteous', 'Sumptuous', 'Benign', 'Anthology', 'Trite', 'Pestilence', 'Pedantic', 'Animosity', 'Pecuniary', 'Tenacious', 'Levity', 'Brevity', 'Melodic', 'Platonic', 'Apt', 'Jargon', 'Svelte', 'Riven', 'Marquee', 'Covet', 'Modesty', 'Sabbatical', 'Tyranny', 'Sumptuous', 'Insolvent', 'Interlude', 'Eclectic', 'Polyglot', 'Reconsecrate', 'Emissary', 'Chesm', 'Tantalizing', 'Eccentric', 'Dour', 'Atoning', 'Destitute', 'nefarious', 'paternalistic', 'Laborious', 'Contentious', 'Pittance', 'Edifice', 'Hedonistic', 'Destitute', 'Fickle', 'Notoriety', 'Enigmatic', 'Ghoulish', 'Posterity', 'Dilapidated', 'Retribution'])


mydoc = docx.Document()
