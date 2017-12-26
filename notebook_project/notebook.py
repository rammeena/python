''' This module creates a new note and performs various operations on
collection of notes'''
import datetime

#Store the next available id for all new notes

last_id = 0

class Note:
    '''Represent a note in notebook. Match against a string in searches
       and store tags for each note.'''

    def __init__(self, memo, tags=''):
        '''Initialize a note with  memo and optional space seperated tags.
           Automatically sets the note creation date and  a unique id
        '''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def search_match(self, search_string):
        '''Determine if note matches the filter text.
        Return True if it matches, False otherwise.

        Search is case sensitive  and matches both  text.
        and tags. '''

        return  search_string in self.memo or  search_string in self.tags

class NoteBook:
    '''Represent a collection of notes that can be tagged, searched
    and modified.'''

    def __init__(self):
        '''Initialize a notebook with empty list'''
        self.notes = []

    def create_note(self, memo, tags=''):
        '''create a new note and add it to the list.'''
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        '''Locate the note with given id'''
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def modify_note(self, note_id, memo):
        '''Find the note with given id and change its memo to the given value'''
        note = self._find_note(note_id)

        if note:
            note.memo = memo
            return True
        return False


    def modify_tags(self, note_id, tags=''):
        '''Find the note with given id and changs its tags with given values'''
        self._find_note(note_id).tags = tags


    def search_notes(self, search_string):
        '''find all notes that match the given filter string'''
        return [note for note in self.notes if note.search_match(search_string)]
