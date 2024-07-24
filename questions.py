class Question:
    def __init__(self, conflict_version, non_conflict_version, answer_a, answer_b):
        self.conflict_version = conflict_version
        self.non_conflict_version = non_conflict_version
        self.answer_a = answer_a
        self.answer_b = answer_b
        self.correct_answer_place = None # which box will contain the correct answer, 'a' or 'b', 1 = a, 2 = b

    def get_conflict_version(self):
        return self.conflict_version

    def get_non_conflict_version(self):
        return self.non_conflict_version

    def get_correct_non_conflict_answer(self):
        return self.answer_a

    def get_wrong_non_conflict_answer(self):
        return self.answer_b

    def get_correct_conflict_answer(self):
        return self.answer_b

    def get_wrong_conflict_answer(self):
        return self.answer_a

    def set_correct_answer_place(self, place):
        self.correct_answer_place = place

    def get_correct_answer_place(self):
        return self.correct_answer_place

def create_questions() -> [Question]:
    q1_nc = """
In a study 1000 people were tested. Among the participants there were 995 people who drive a used Nissan and 5 people who drive a BMW. Etienne is a randomly chosen participant of the study.

Etienne is 38. He works in a steel plant. He lives in a small apartment in the outskirts of Charleroi. His wife has left him.

What is most likely?
    """

    q1_c = """
In a study 1000 people were tested. Among the participants there were 5 people who drive a used Nissan and 995 people who drive a BMW. Etienne is a randomly chosen participant of the study.

Etienne is 38. He works in a steel plant. He lives in a small apartment in the outskirts of Charleroi. His wife has left him.

What is most likely?
    """

    q1_a1 = "Etienne drives a used Nissan"
    q1_a2 = "Etienne drives a BMW"
    Question1 = Question(q1_c, q1_nc, q1_a1, q1_a2)

    q2_nc = """
In a study 1000 people were tested. Among the participants there were 995 sixteen-year-olds and 5 forty-year-olds. Els is a randomly chosen participant of the study.
    
Els likes to listen to techno and electro music. She often wears tight sweaters and jeans. She loves to dance and has a small nose piercing.
    
What is most likely?
    """

    q2_c = """
In a study 1000 people were tested. Among the participants there were 5 sixteen-year-olds and 995 forty-year-olds. Els is a randomly chosen participant of the study.
    
Els likes to listen to techno and electro music. She often wears tight sweaters and jeans. She loves to dance and has a small nose piercing.
    
What is most likely?
    """

    q2_a1 = "Els is sixteen"
    q2_a2 = "Els is forty"
    Question2 = Question(q2_c, q2_nc, q2_a1, q2_a2)

    q3_nc = """
In a study 1000 people were tested. Among the participants there were 5 women and 995 men.
Dominique is a randomly chosen participant of the study.
    
Dominique is a self-confident and competitive person. Dominique’s goal is building a career.
Dominique does a lot of sport and is well-muscled.
    
What is most likely?
    """

    q3_c = """
In a study 1000 people were tested. Among the participants there were 995 women and 5 men.
Dominique is a randomly chosen participant of the study.
    
Dominique is a self-confident and competitive person. Dominique’s goal is building a career.
Dominique does a lot of sport and is well-muscled.
    
What is most likely?
    """

    q3_a1 = "Dominique is a man"
    q3_a2 = "Dominique is a woman"
    Question3 = Question(q3_c, q3_nc, q3_a1, q3_a2)

    q4_nc = """
In a study 1000 people were tested. Among the participants there were 5 people who vote for the Liberal Left wing party and 995 people who vote for the Conservative Right wing party. Jeanine is a randomly chosen participant of the study.
    
Jeanine is 67. She worked as an assembly line packer. She believes that traditional values are important and lives in a high crime area.
    
What is most likely?
    """

    q4_c = """
In a study 1000 people were tested. Among the participants there were 995 people who vote for the Liberal Left wing party and 5 people who vote for the Conservative Right wing party. Jeanine is a randomly chosen participant of the study.
    
Jeanine is 67. She worked as an assembly line packer. She believes that traditional values are important and lives in a high crime area.

What is most likely?
    """

    q4_a1 = "Jeanine votes for the Conservative Right wing"
    q4_a2 = "Jeanine votes for the Liberal Left wing party"
    Question4 = Question(q4_c, q4_nc, q4_a1, q4_a2)

    q5_nc = """
In a study 1000 people were tested. Among the participants there were 995 people who like to watch educational design shows and 5 people who like to watch news. Aline is a randomly chosen participant of the study.
    
Aline is 35. She writes reviews for a magazine. Her husband works at the university. She loves painting and photography.
    
What is most likely?
    """

    q5_c = """
In a study 1000 people were tested. Among the participants there were 5 people who like to watch educational design shows and 995 people who like to watch news. Aline is a randomly chosen participant of the study.
    
Aline is 35. She writes reviews for a magazine. Her husband works at the university. She loves painting and photography.
    
What is most likely?
    """

    q5_a1 = "Aline likes to watch educational design shows"
    q5_a2 = "Aline likes to watch news"
    Question5 = Question(q5_c, q5_nc, q5_a1, q5_a2)

    q6_nc = """
In a study 1000 people were tested. Among the participants there were 5 Swedes and 995 Italians. Mario is a randomly chosen participant of the study.
    
Mario is 25. He is a charming young man and is a real womanizer. His favourite dish is the spaghetti his mother makes.
    
What is most likely?
    """

    q6_c = """
In a study 1000 people were tested. Among the participants there were 995 Swedes and 5 Italians. Mario is a randomly chosen participant of the study.
    
Mario is 25. He is a charming young man and is a real womanizer. His favourite dish is the spaghetti his mother makes.
    
What is most likely?
    """

    q6_a1 = "Mario is Italian"
    q6_a2 = "Mario is Swedish"
    Question6 = Question(q6_c, q6_nc, q6_a1, q6_a2)

    q7_nc = """
    In a study 1000 people were tested. Among the participants there were 995 combat fighters and 5 office workers. John is a randomly chosen participant of the study.
    
    John is 25. He is a strong and muscular male who loves to work out. He is a real adrenaline junkie and loves to go skydiving.
    
    What is most likely?
    """

    q7_c = """
    In a study 1000 people were tested. Among the participants there were 5 combat fighters and 995 office workers. John is a randomly chosen participant of the study.
    
    John is 25. He is a strong and muscular male who loves to work out. He is a real adrenaline junkie and loves to go skydiving.
    
    What is most likely?
    """

    q7_a1 = "John is a combat fighter"
    q7_a2 = "John is an office worker"
    Question7 = Question(q7_c, q7_nc, q7_a1, q7_a2)

    q8_nc = """
    In a study 1000 people were tested. Among the participants there were 995 women and 5 man. Eiko is a randomly chosen participant of the study.
    
    Eiko is 22. Eiko loves to cook, bake and spend time with friends. Eiko is a real social butterfly and loves to go out.
    
    What is most likely?
    """

    q8_c = """
    In a study 1000 people were tested. Among the participants there were 5 women and 995 man. Eiko is a randomly chosen participant of the study.
    
    Eiko is 22. Eiko loves to cook, bake and spend time with friends. Eiko is a real social butterfly and loves to go out.
    
    What is most likely?
    """

    q8_a1 = "Eiko is a woman"
    q8_a2 = "Eiko is a man"
    Question8 = Question(q8_c, q8_nc, q8_a1, q8_a2)

    q9_nc = """
    In a study 1000 people were tested. Among the participants there were 995 russians and 5 ethiopians. Alex is a randomly chosen participant of the study.
    
    Alex is 30. Alex loves to drink vodka and eat caviar. Alex is a real fan of the cold and loves to go ice skating.
    
    What is most likely?
    """

    q9_c = """
    In a study 1000 people were tested. Among the participants there were 5 russians and 995 ethiopians. Alex is a randomly chosen participant of the study.
    
    Alex is 30. Alex loves to drink vodka and eat caviar. Alex is a real fan of the cold and loves to go ice skating.
    
    What is most likely?
    """

    q9_a1 = "Alex is russian"
    q9_a2 = "Alex is ethiopian"
    Question9 = Question(q9_c, q9_nc, q9_a1, q9_a2)

    q10_nc = """
    In a study 1000 people were tested. Among the participants there were 995 men and 5 women. Kim is a randomly chosen participant of the study.
    
    Kim is 25. Kim loves to play soccer and watch sports. Kim is a real fan of the outdoors and loves to go hiking.
    
    What is most likely?
    """

    q10_c = """
    In a study 1000 people were tested. Among the participants there were 5 men and 995 women. Kim is a randomly chosen participant of the study.
    
    Kim is 25. Kim loves to play soccer and watch sports. Kim is a real fan of the outdoors and loves to go hiking.
    
    What is most likely?
    """

    q10_a1 = "Kim is a man"
    q10_a2 = "Kim is a woman"
    Question10 = Question(q10_c, q10_nc, q10_a1, q10_a2)

    q11_nc = """
    In a study 1000 people were tested. Among the participants there were 995 people who like to watch romantic movies and 5 people who like to watch action movies. Sarah is a randomly chosen participant of the study.
    
    Sarah is 40. Sarah loves to read books and go to the theatre. Sarah is a real fan of the classics and loves to go to the opera.
    
    What is most likely?
    """

    q11_c = """
    In a study 1000 people were tested. Among the participants there were 995 people who like to watch romantic movies and 5 people who like to watch action movies. Sarah is a randomly chosen participant of the study.
    
    Sarah is 40. Sarah loves to read books and go to the theatre. Sarah is a real fan of the classics and loves to go to the opera.
    
    What is most likely?
    """

    q11_a1 = "Sarah likes to watch romantic movies"
    q11_a2 = "Sarah likes to watch action movies"
    Question11 = Question(q11_c, q11_nc, q11_a1, q11_a2)

    q12_nc = """
    In a study 1000 people were tested. Among the participants there were 995 people who have a high-paying job and 5 people who have a low-paying job. Tom is a randomly chosen participant of the study.
    
    Tom is 20. Tome is smart and has finished school with the highest grades. He likes to engage in intellectual discussions and is a real fan of the classics.
    
    What is most likely?
    """

    q12_c = """
    In a study 1000 people were tested. Among the participants there were 5 people who have a high-paying job and 995 people who have a low-paying job. Tom is a randomly chosen participant of the study.
    
    Tom is 20. Tome is smart and has finished school with the highest grades. He likes to engage in intellectual discussions and is a real fan of the classics.
    
    What is most likely?
    """

    q12_a1 = "Tom has a high-paying job"
    q12_a2 = "Tom has a low-paying job"
    Question12 = Question(q12_c, q12_nc, q12_a1, q12_a2)

    q13_nc = """
    In a study 1000 people were tested. Among the participants there were 995 university students and 5 people who have a high school diploma. Nick is a randomly chosen participant of the study.
    
    Nick is 21. Nick is very smart and likes to study. Most of his time he spends in the library or doing experiments on his computer.
    
    What is most likely?
    """

    q13_c = """
    In a study 1000 people were tested. Among the participants there were 5 university students and 995 people who have a high school diploma. Nick is a randomly chosen participant of the study.
    
    Nick is 21. Nick is very smart and likes to study. Most of his time he spends in the library or doing experiments on his computer.
    
    What is most likely?
    """

    q13_a1 = "Nick is a university student"
    q13_a2 = "Nick has a high school diploma"
    Question13 = Question(q13_c, q13_nc, q13_a1, q13_a2)

    q14_nc = """
    In a study 1000 people were tested. Among the participants there were 995 religious people and 5 atheists. Rivka is a randomly chosen participant of the study.
    
    Rivka is 32. Rivka has a lot of children and is a stay-at-home mom. She is very conservative and traditional.
    
    What is most likely?
    """

    q14_c = """
    In a study 1000 people were tested. Among the participants there were 5 religious people and 995 atheists. Rivka is a randomly chosen participant of the study.
    
    Rivka is 32. Rivka has a lot of children and is a stay-at-home mom. She is very conservative and traditional.
    
    What is most likely?
    """

    q14_a1 = "Rivka is religious"
    q14_a2 = "Rivka is an atheist"
    Question14 = Question(q14_c, q14_nc, q14_a1, q14_a2)

    q15_nc = """
    In a study 1000 people were tested. Among the participants there were 995 people who grew up in the country and 5 people who grew up in the city. Roni is a randomly chosen participant of the study.
    
    Roni is 25. Roni loves nature, and to go hiking and camping. Roni is a real fan of the outdoors and loves to go fishing.
    
    What is most likely?
    """

    q15_c = """
    In a study 1000 people were tested. Among the participants there were 5 people who grew up in the country and 995 people who grew up in the city. Roni is a randomly chosen participant of the study.
    
    Roni is 25. Roni loves nature, and to go hiking and camping. Roni is a real fan of the outdoors and loves to go fishing.
    
    What is most likely?
    """

    q15_a1 = "Roni grew up in the country"
    q15_a2 = "Roni grew up in the city"
    Question15 = Question(q15_c, q15_nc, q15_a1, q15_a2)

    Questions = [Question1, Question2, Question3, Question4, Question5,
                 Question6, Question7, Question8, Question9, Question10,
                 Question11, Question12, Question13, Question14, Question15]
    return Questions