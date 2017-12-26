class NoteBook:
    '''Class to create a new notebook'''

    def __init__(self):
        '''function to initiate containers for storing nodes'''
        self.notes = {}
        self.notes_list = []

    def add_note(self, note_name, note_desc="Its a Empty Note"):
        '''method to add a new note to notebook'''
        self.notes_list.append(note_name)
        self.notes[note_name] = note_desc

    def search_note(self, note_name):
        '''method to seach notes'''
        if self.notes.get(note_name):
            print("Note:'", note_name, "' is available")

    def read_note(self, note_name):
        '''method to read notes'''
        print(self.notes[note_name])

    def delete_note(self, note_name):
        '''method to delete notes'''
        if self.notes.pop(note_name, None):
            self.notes_list.pop(note_name)
            print(note_name, 'deleted')
        else:
            print("Note:'", note_name, "' is not available")
