import streamlit as st
import pandas as pd
import requests

def load_and_process_csv():
    st.title("Traitement des Salons")
    
    # Upload du fichier (CSV ou Excel)
    uploaded_file = st.file_uploader(
        "Choisissez votre fichier (CSV, XLS, XLSX)", 
        type=["csv", "xls", "xlsx"]
    )
    
    if uploaded_file is not None:
        # Lecture du fichier selon son type
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
                
            # Sélection de la colonne contenant les salons
            column_name = st.selectbox("Sélectionnez la colonne des salons", df.columns)
            
            if column_name:
                # Récupération de la liste unique des salons
                salons = df[column_name].unique().tolist()
                
                # Affichage et sélection des salons
                st.subheader("Sélection des salons à traiter")
                

                selected_salons = st.multiselect(
                    "Choisissez les salons à traiter",
                    salons,
                    default=salons
                )
                # Sélection du rôle
                selected_roles = st.multiselect(
                    "Sélectionnez les rôles",
                    ["Directeur Général", "Président", "Co-fondateur", "Directeur Commercial", "Directeur Marketing", "Directeur Financier", "Directeur des Opérations", "Directeur Technique"],
                    default=["Directeur Général"]
                )

                # Champ pour les emails des destinataires
                recipient_emails = st.text_input(
                    "Entrez une adresse email du destinataires",
                    placeholder="exemple1@domaine.com"
                )

                # Bouton pour lancer le traitement
                if st.button("Lancer le traitement"):
                    if selected_salons:
                        # Préparation des données pour Make
                        payload = {"salons": selected_salons,"role":selected_roles,"emails":recipient_emails}
                        
                        
                        try:
                            # Utilisation du webhook depuis les secrets
                            response = requests.post(
                                st.secrets["MAKE_WEBHOOK_URL"],
                                json=payload
                            )
                            
                            if response.status_code == 200:
                                st.success("Traitement lancé avec succès!")
                                st.info("Vous recevrez un email une fois le traitement terminé.")
                            else:
                                print(response.status_code)
                                st.error("Erreur lors de l'envoi des données.")
                        
                        except Exception as e:
                            st.error(f"Erreur de connexion: {str(e)}")
                    else:
                        st.warning("Veuillez sélectionner au moins un salon.")
        except Exception as e:
            st.error(f"Erreur lors de la lecture du fichier: {str(e)}")

if __name__ == "__main__":
    load_and_process_csv()
