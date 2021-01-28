class EmailSlicer:
    def __init__(self, email, username):
        self.email = email
        self.username = username

    
    def domains(self):
        user_email = self.email
        index_at = user_email.find('@') + 1 # 1º argumento é inclusivo e queremos que ele comece a fatia depois do @
        index_dot_after_at = user_email.find('.', index_at)
        domain_email_plataform = user_email[index_at:index_dot_after_at]
        return domain_email_plataform, print(domain_email_plataform)
    



email = EmailSlicer('gustavopfpereira30@gmail.com', 'Gustavo')
email.domains()


#  def welcome(self):
#         name_user = input("Hello! What's is you name?")
#         print(f'Welcome to email slicer {name_user}!')
        
#         return email