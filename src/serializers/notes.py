class NoteSerializer:
    @classmethod
    def note_entity(cls, note) -> dict:
        return {
            "id": str(note["_id"]),
            "title": note["title"],
            "category": note["category"],
            "content": note["content"],
            "published": note["published"],
            "createdAt": note["createdAt"],
            "updatedAt": note["updatedAt"],
        }

    @classmethod
    def note_list_entity(cls, notes) -> list:
        return [cls.note_entity(note) for note in notes]
