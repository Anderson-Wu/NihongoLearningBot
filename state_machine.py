#  for mail

# state "vocabulary_export_favorite","vocabulary_export_favorite_email","vocabulary_export_favorite_email_complete",
# transition
# {
#     "trigger": "advance",
#     "source": "vocabulary",
#     "dest": "vocabulary_export_favorite",
#     "conditions": "is_going_to_vocabulary_export_favorite",
# },
# {
#     "trigger": "advance",
#     "source": "vocabulary_export_favorite",
#     "dest": "vocabulary_export_favorite_email",
#     "conditions": "is_going_to_vocabulary_export_favorite_email",
# },
# {
#     "trigger": "advance",
#     "source": "vocabulary_export_favorite_email",
#     "dest": "vocabulary_export_favorite_email_complete",
#     "conditions": "is_going_to_vocabulary_export_favorite_email_complete",
# },
# {"trigger": "go_back_vocabulary",
#  "source": ["vocabulary_n2", "vocabulary_n3", "vocabulary_n4", "vocabulary_n5", "vocabulary_favorite",
#             "vocabulary_export_favorite_email_complete"], "dest": "vocabulary"},

machine_diagram_states = ["user", "vocabulary", "vocabulary_n2", "vocabulary_n3", "vocabulary_n4", "vocabulary_n5",
                          "vocabulary_favorite", "vocabulary_add_favorite",
                          "vocabulary_delete_favorite", "vocabulary_test", "vocabulary_test_type",
                          "vocabulary_test_type_level_2", "vocabulary_test_type_level_3",
                          "vocabulary_test_type_level_4", "vocabulary_test_type_level_5",
                          "vocabulary_test_type_level_2_answer", "vocabulary_test_type_level_3_answer",
                          "vocabulary_test_type_level_4_answer", "vocabulary_test_type_level_5_answer"]
machine_diagram_transitions = [
    {
        "trigger": "advance",
        "source": "user",
        "dest": "vocabulary",
        "conditions": "is_going_to_vocabulary",
    },
    {
        "trigger": "advance",
        "source": "vocabulary",
        "dest": "vocabulary_n2",
        "conditions": "is_going_to_vocabulary_n2",
    },
    {
        "trigger": "advance",
        "source": "vocabulary",
        "dest": "vocabulary_n3",
        "conditions": "is_going_to_vocabulary_n3",
    },
    {
        "trigger": "advance",
        "source": "vocabulary",
        "dest": "vocabulary_n4",
        "conditions": "is_going_to_vocabulary_n4",
    },
    {
        "trigger": "advance",
        "source": "vocabulary",
        "dest": "vocabulary_n5",
        "conditions": "is_going_to_vocabulary_n5",
    },
    {
        "trigger": "advance",
        "source": "vocabulary_n2",
        "dest": "vocabulary_n2",
        "conditions": "is_going_to_vocabulary_n2",
    },
    {
        "trigger": "advance",
        "source": "vocabulary_n3",
        "dest": "vocabulary_n3",
        "conditions": "is_going_to_vocabulary_n3",
    },
    {
        "trigger": "advance",
        "source": "vocabulary_n4",
        "dest": "vocabulary_n4",
        "conditions": "is_going_to_vocabulary_n4",
    },
    {
        "trigger": "advance",
        "source": "vocabulary_n5",
        "dest": "vocabulary_n5",
        "conditions": "is_going_to_vocabulary_n5",
    },
    {
        "trigger": "advance",
        "source": "vocabulary_n2",
        "dest": "vocabulary_add_favorite",
        "conditions": "is_going_to_vocabulary_add_favorite",
    },
    {
        "trigger": "advance",
        "source": "vocabulary_n3",
        "dest": "vocabulary_add_favorite",
        "conditions": "is_going_to_vocabulary_add_favorite",
    },
    {
        "trigger": "advance",
        "source": "vocabulary_n4",
        "dest": "vocabulary_add_favorite",
        "conditions": "is_going_to_vocabulary_add_favorite",
    },
    {
        "trigger": "advance",
        "source": "vocabulary_n5",
        "dest": "vocabulary_add_favorite",
        "conditions": "is_going_to_vocabulary_add_favorite",
    },
    {
        "trigger": "advance",
        "source": "vocabulary",
        "dest": "vocabulary_favorite",
        "conditions": "is_going_to_vocabulary_favorite",
    },
    {
        "trigger": "advance",
        "source": "vocabulary_favorite",
        "dest": "vocabulary_favorite",
        "conditions": "is_going_to_vocabulary_favorite",
    },
    {
        "trigger": "advance",
        "source": "vocabulary_favorite",
        "dest": "vocabulary_delete_favorite",
        "conditions": "is_going_to_vocabulary_delete_favorite",
    },

    {
        "trigger": "advance",
        "source": "vocabulary",
        "dest": "vocabulary_test",
        "conditions": "is_going_to_vocabulary_test",
    },
    {
        "trigger": "advance",
        "source": "vocabulary_test",
        "dest": "vocabulary_test_type",
        "conditions": "is_going_to_vocabulary_test_type",
    },
    {
        "trigger": "advance",
        "source": "vocabulary_test_type",
        "dest": "vocabulary_test_type_level_2",
        "conditions": "is_going_to_vocabulary_test_type_level_2",
    },
    {
        "trigger": "advance",
        "source": "vocabulary_test_type",
        "dest": "vocabulary_test_type_level_3",
        "conditions": "is_going_to_vocabulary_test_type_level_3",
    },
    {
        "trigger": "advance",
        "source": "vocabulary_test_type",
        "dest": "vocabulary_test_type_level_4",
        "conditions": "is_going_to_vocabulary_test_type_level_4",
    },
    {
        "trigger": "advance",
        "source": "vocabulary_test_type",
        "dest": "vocabulary_test_type_level_5",
        "conditions": "is_going_to_vocabulary_test_type_level_5",
    },
    {
        "trigger": "advance",
        "source": "vocabulary_test_type_level_2",
        "dest": "vocabulary_test_type_level_2_answer",
        "conditions": "is_going_to_vocabulary_test_type_level_2_answer",
    },
    {
        "trigger": "advance",
        "source": "vocabulary_test_type_level_3",
        "dest": "vocabulary_test_type_level_3_answer",
        "conditions": "is_going_to_vocabulary_test_type_level_3_answer",
    },
    {
        "trigger": "advance",
        "source": "vocabulary_test_type_level_4",
        "dest": "vocabulary_test_type_level_4_answer",
        "conditions": "is_going_to_vocabulary_test_type_level_4_answer",
    },
    {
        "trigger": "advance",
        "source": "vocabulary_test_type_level_5",
        "dest": "vocabulary_test_type_level_5_answer",
        "conditions": "is_going_to_vocabulary_test_type_level_5_answer",
    },
    {
        "trigger": "advance",
        "source": "vocabulary_test_type_level_2_answer",
        "dest": "vocabulary_test_type_level_2",
        "conditions": "is_going_to_vocabulary_test_type_level_2",
    },
    {
        "trigger": "advance",
        "source": "vocabulary_test_type_level_3_answer",
        "dest": "vocabulary_test_type_level_3",
        "conditions": "is_going_to_vocabulary_test_type_level_3",
    },
    {
        "trigger": "advance",
        "source": "vocabulary_test_type_level_4_answer",
        "dest": "vocabulary_test_type_level_4",
        "conditions": "is_going_to_vocabulary_test_type_level_4",
    },
    {
        "trigger": "advance",
        "source": "vocabulary_test_type_level_5_answer",
        "dest": "vocabulary_test_type_level_5",
        "conditions": "is_going_to_vocabulary_test_type_level_5",
    },
    {
        "trigger": "advance",
        "source": "vocabulary_test_type_level_2_answer",
        "dest": "vocabulary",
        "conditions": "is_going_to_vocabulary",
    },
    {
        "trigger": "advance",
        "source": "vocabulary_test_type_level_2_answer",
        "dest": "vocabulary_add_favorite",
        "conditions": "is_going_to_vocabulary_add_favorite",
    },
    {
        "trigger": "advance",
        "source": "vocabulary_test_type_level_3_answer",
        "dest": "vocabulary",
        "conditions": "is_going_to_vocabulary",
    },
    {
        "trigger": "advance",
        "source": "vocabulary_test_type_level_3_answer",
        "dest": "vocabulary_add_favorite",
        "conditions": "is_going_to_vocabulary_add_favorite",
    },
    {
        "trigger": "advance",
        "source": "vocabulary_test_type_level_4_answer",
        "dest": "vocabulary",
        "conditions": "is_going_to_vocabulary",
    },
    {
        "trigger": "advance",
        "source": "vocabulary_test_type_level_4_answer",
        "dest": "vocabulary_add_favorite",
        "conditions": "is_going_to_vocabulary_add_favorite",
    },
    {
        "trigger": "advance",
        "source": "vocabulary_test_type_level_5_answer",
        "dest": "vocabulary",
        "conditions": "is_going_to_vocabulary",
    },
    {
        "trigger": "advance",
        "source": "vocabulary_test_type_level_5_answer",
        "dest": "vocabulary_add_favorite",
        "conditions": "is_going_to_vocabulary_add_favorite",
    },
    {"trigger": "go_back_vocabulary",
     "source": ["vocabulary_n2", "vocabulary_n3", "vocabulary_n4", "vocabulary_n5", "vocabulary_favorite"],
     "dest": "vocabulary"},
    {"trigger": "go_back_vocabulary_test_type_level_2_answer", "source": ["vocabulary_add_favorite"],
     "dest": "vocabulary_test_type_level_2_answer"},
    {"trigger": "go_back_vocabulary_test_type_level_3_answer", "source": ["vocabulary_add_favorite"],
     "dest": "vocabulary_test_type_level_3_answer"},
    {"trigger": "go_back_vocabulary_test_type_level_4_answer", "source": ["vocabulary_add_favorite"],
     "dest": "vocabulary_test_type_level_4_answer"},
    {"trigger": "go_back_vocabulary_test_type_level_5_answer", "source": ["vocabulary_add_favorite"],
     "dest": "vocabulary_test_type_level_5_answer"},
    {"trigger": "go_back_vocabulary_n2", "source": ["vocabulary_add_favorite"], "dest": "vocabulary_n2"},
    {"trigger": "go_back_vocabulary_n3", "source": ["vocabulary_add_favorite"], "dest": "vocabulary_n3"},
    {"trigger": "go_back_vocabulary_n4", "source": ["vocabulary_add_favorite"], "dest": "vocabulary_n4"},
    {"trigger": "go_back_vocabulary_n5", "source": ["vocabulary_add_favorite"], "dest": "vocabulary_n5"},
    {"trigger": "go_back_favorite", "source": ["vocabulary_delete_favorite"], "dest": "vocabulary_favorite"},

]