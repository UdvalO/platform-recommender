def get_yes_no_input(question):
    """Helper function to get valid yes/no input from user"""
    while True:
        response = input(f"{question} (yes/no): ").lower().strip()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'")


def recommend_platform_interactive():
    """
    Interactive function that asks questions and recommends a platform based on user responses.
    Returns the recommendation and the decision path taken.
    """
    decision_path = []

    print("\nPlease select the type of data you'll be working with:")
    print("1. Digital data only")
    print("2. Questionnaire only")
    print("3. Combined data")

    while True:
        choice = input("\nEnter your choice (1-3): ").strip()
        if choice in ['1', '2', '3']:
            break
        print("Please enter a valid choice (1-3)")

    data_types = {
        '1': 'Digital data only',
        '2': 'Questionnaire only',
        '3': 'Combined data'
    }

    data_type = data_types[choice]
    decision_path.append(f"Data Type: {data_type}")

    # Handle different data type paths
    if data_type == 'Digital data only':
        has_coding = get_yes_no_input("\nDo you have coding skills?")
        decision_path.append(f"Has coding skills: {'Yes' if has_coding else 'No'}")

        if has_coding:
            recommendation = "Google Fit API schema"
        else:
            recommendation = "Manual data export from wearables"

    elif data_type == 'Questionnaire only':
        has_coding = get_yes_no_input("\nDo you have basic coding skills?")
        decision_path.append(f"Has coding skills: {'Yes' if has_coding else 'No'}")

        if has_coding:
            recommendation = "FormR"
        else:
            recommendation = "Google Form"

    else:  # Combined data
        has_coding = get_yes_no_input("\nDo you have basic coding skills?")
        decision_path.append(f"Has coding skills: {'Yes' if has_coding else 'No'}")

        if not has_coding:
            recommendation = "Google Form + Manual Data Export from Wearables"
        else:
            wants_robust = get_yes_no_input("\nDo you want robust wearables data integration?")
            decision_path.append(f"Wants robust integration: {'Yes' if wants_robust else 'No'}")

            if wants_robust:
                wants_complex = get_yes_no_input("\nDo you want better features but more complex setup?")
                decision_path.append(f"Wants complex setup with better features: {'Yes' if wants_complex else 'No'}")

                if wants_complex:
                    wants_training = get_yes_no_input("\nDo you want hands-on training?")
                    decision_path.append(f"Wants hands-on training: {'Yes' if wants_training else 'No'}")

                    if wants_training:
                        recommendation = "RADAR-base"
                    else:
                        recommendation = "LAMP platform"
                else:
                    wants_easier = get_yes_no_input("\nDo you want easier setup but less features?")
                    decision_path.append(f"Wants easier setup with less features: {'Yes' if wants_easier else 'No'}")

                    if wants_easier:
                        recommendation = "LAMP platform"
                    else:
                        recommendation = "RADAR-base"
            else:
                wants_support = get_yes_no_input("\nDo you want technical support?")
                decision_path.append(f"Wants technical support: {'Yes' if wants_support else 'No'}")

                if not wants_support:
                    recommendation = "Open mHealth"
                else:
                    wants_training = get_yes_no_input("\nDo you want hands-on training?")
                    decision_path.append(f"Wants hands-on training: {'Yes' if wants_training else 'No'}")

                    if wants_training:
                        has_staff = get_yes_no_input("\nDo you have university staff to support your project?")
                        decision_path.append(f"Has university staff: {'Yes' if has_staff else 'No'}")

                        recommendation = "REDCap" if has_staff else "PsychoPy"
                    else:
                        recommendation = "Open mHealth"

    return recommendation, decision_path



def display_results(recommendation, decision_path, session_number):
    """Display the recommendation and decision path in a clear format"""
    print("\n" + "=" * 50)
    print(f"RECOMMENDATION RESULTS (Session {session_number})")
    print("=" * 50)
    print("\nDecision Path:")
    for i, decision in enumerate(decision_path, 1):
        print(f"{i}. {decision}")
    print("\nRecommended Platform:", recommendation)
    print("=" * 50)


def run_recommendation_session():
    """Main function to run multiple recommendation sessions"""
    session_number = 1
    all_recommendations = []

    print("\nWelcome to the Platform Recommender!")

    while True:
        # Run a recommendation session
        recommendation, path = recommend_platform_interactive()
        display_results(recommendation, path, session_number)

        # Store the results
        all_recommendations.append({
            'session': session_number,
            'recommendation': recommendation,
            'path': path
        })

        # Ask if user wants to try another data type
        if not get_yes_no_input("\nWould you like to try another data type?"):
            break

        session_number += 1
        print("\n" + "-" * 50)
        print("Starting new recommendation session...")
        print("-" * 50)

    # Display summary of all sessions
    print("\n" + "=" * 50)
    print("SUMMARY OF ALL RECOMMENDATIONS")
    print("=" * 50)
    for session in all_recommendations:
        print(f"\nSession {session['session']}:")
        print(f"Recommended Platform: {session['recommendation']}")
        print(f"Data Type: {session['path'][0]}")
        print("-" * 30)


if __name__ == "__main__":
    try:
        run_recommendation_session()
        print("\nThank you for using the Platform Recommender!")
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")
    except Exception as e:
        print(f"\n\nAn error occurred: {e}")
