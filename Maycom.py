import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

class MayotteCommuneFinanceAnalyzer:
    def __init__(self, commune_name):
        self.commune = commune_name
        self.colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#F9A602', '#6A0572', 
                      '#AB83A1', '#5CAB7D', '#2A9D8F', '#E76F51', '#264653']
        
        self.start_year = 2002
        self.end_year = 2025
        
        # Configuration spécifique à chaque commune
        self.config = self._get_commune_config()
        
    def _get_commune_config(self):
        """Retourne la configuration spécifique pour chaque commune mahoraise"""
        configs = {
            "Mamoudzou": {
                "population_base": 71000,
                "budget_base": 85,
                "type": "urbaine",
                "specialites": ["administration", "commerce", "sante", "education", "port"]
            },
            "Koungou": {
                "population_base": 35000,
                "budget_base": 65,
                "type": "periurbaine",
                "specialites": ["commerce", "zones_activites", "services", "agriculture_urbaine"]
            },
            "Dzaoudzi": {
                "population_base": 18000,
                "budget_base": 50,
                "type": "urbaine",
                "specialites": ["administration", "port", "tourisme", "histoire"]
            },
            "Sada": {
                "population_base": 12000,
                "budget_base": 40,
                "type": "rurale",
                "specialites": ["agriculture", "elevage", "artisanat", "culture"]
            },
            "Bandrélé": {
                "population_base": 10000,
                "budget_base": 35,
                "type": "cotiere",
                "specialites": ["peche", "tourisme", "agriculture", "plages"]
            },
            "Pamandzi": {
                "population_base": 11000,
                "budget_base": 38,
                "type": "urbaine",
                "specialites": ["aeroport", "administration", "services", "commerce"]
            },
            "Bouéni": {
                "population_base": 6000,
                "budget_base": 30,
                "type": "rurale",
                "specialites": ["agriculture", "peche", "tourisme_vert", "artisanat"]
            },
            "Chiconi": {
                "population_base": 8000,
                "budget_base": 32,
                "type": "rurale",
                "specialites": ["agriculture", "commerce", "services_locaux", "culture"]
            },
            "Tsingoni": {
                "population_base": 15000,
                "budget_base": 45,
                "type": "periurbaine",
                "specialites": ["agriculture", "commerce", "tourisme", "histoire"]
            },
            # Configuration par défaut pour les autres communes
            "default": {
                "population_base": 7000,
                "budget_base": 28,
                "type": "rurale",
                "specialites": ["agriculture", "peche", "petit_commerce", "services_locaux"]
            }
        }
        
        return configs.get(self.commune, configs["default"])
    
    def generate_financial_data(self):
        """Génère des données financières pour la commune"""
        print(f"🏛️ Génération des données financières pour {self.commune}...")
        
        # Créer une base de données annuelle
        dates = pd.date_range(start=f'{self.start_year}-01-01', 
                             end=f'{self.end_year}-12-31', freq='Y')
        
        data = {'Annee': [date.year for date in dates]}
        
        # Données démographiques (croissance très forte à Mayotte)
        data['Population'] = self._simulate_population(dates)
        data['Menages'] = self._simulate_households(dates)
        
        # Recettes communales
        data['Recettes_Totales'] = self._simulate_total_revenue(dates)
        data['Impots_Locaux'] = self._simulate_tax_revenue(dates)
        data['Dotations_Etat'] = self._simulate_state_grants(dates)
        data['Autres_Recettes'] = self._simulate_other_revenue(dates)
        
        # Dépenses communales
        data['Depenses_Totales'] = self._simulate_total_expenses(dates)
        data['Fonctionnement'] = self._simulate_operating_expenses(dates)
        data['Investissement'] = self._simulate_investment_expenses(dates)
        data['Charge_Dette'] = self._simulate_debt_charges(dates)
        data['Personnel'] = self._simulate_staff_costs(dates)
        
        # Indicateurs financiers
        data['Epargne_Brute'] = self._simulate_gross_savings(dates)
        data['Dette_Totale'] = self._simulate_total_debt(dates)
        data['Taux_Endettement'] = self._simulate_debt_ratio(dates)
        data['Taux_Fiscalite'] = self._simulate_tax_rate(dates)
        
        # Investissements spécifiques adaptés à Mayotte
        data['Investissement_Agriculture'] = self._simulate_agriculture_investment(dates)
        data['Investissement_Peche'] = self._simulate_fishing_investment(dates)
        data['Investissement_Transport'] = self._simulate_transport_investment(dates)
        data['Investissement_Education'] = self._simulate_education_investment(dates)
        data['Investissement_Sante'] = self._simulate_health_investment(dates)
        data['Investissement_Environnement'] = self._simulate_environment_investment(dates)
        
        df = pd.DataFrame(data)
        
        # Ajouter des tendances spécifiques à la commune mahoraise
        self._add_municipal_trends(df)
        
        return df
    
    def _simulate_population(self, dates):
        """Simule la population de la commune (croissance très forte à Mayotte)"""
        base_population = self.config["population_base"]
        
        population = []
        for i, date in enumerate(dates):
            # Croissance démographique très forte à Mayotte
            if self.config["type"] == "urbaine":
                growth_rate = 0.045  # Croissance urbaine très forte
            elif self.config["type"] == "periurbaine":
                growth_rate = 0.048  # Croissance périurbaine encore plus forte
            else:  # rurale
                growth_rate = 0.042  # Croissance rurale très forte
                
            growth = 1 + growth_rate * i
            population.append(base_population * growth)
        
        return population
    
    def _simulate_households(self, dates):
        """Simule le nombre de ménages"""
        base_households = self.config["population_base"] / 3.5  # Taille des ménages plus grande
        
        households = []
        for i, date in enumerate(dates):
            growth = 1 + 0.038 * i  # Croissance très forte
            households.append(base_households * growth)
        
        return households
    
    def _simulate_total_revenue(self, dates):
        """Simule les recettes totales de la commune"""
        base_revenue = self.config["budget_base"]
        
        revenue = []
        for i, date in enumerate(dates):
            # Croissance variable selon le type de commune
            if self.config["type"] == "urbaine":
                growth_rate = 0.055  # Croissance très forte à Mayotte
            elif self.config["type"] == "periurbaine":
                growth_rate = 0.058  # Croissance encore plus forte
            else:  # rurale
                growth_rate = 0.048  # Croissance rurale forte
                
            growth = 1 + growth_rate * i
            noise = np.random.normal(1, 0.09)  # Plus de volatilité
            revenue.append(base_revenue * growth * noise)
        
        return revenue
    
    def _simulate_tax_revenue(self, dates):
        """Simule les recettes fiscales"""
        base_tax = self.config["budget_base"] * 0.30  # Part plus faible des impôts locaux
        
        tax_revenue = []
        for i, date in enumerate(dates):
            growth = 1 + 0.035 * i  # Croissance forte
            noise = np.random.normal(1, 0.10)  # Plus de volatilité
            tax_revenue.append(base_tax * growth * noise)
        
        return tax_revenue
    
    def _simulate_state_grants(self, dates):
        """Simule les dotations de l'État (très importantes à Mayotte)"""
        base_grants = self.config["budget_base"] * 0.55  # Part très importante des dotations
        
        grants = []
        for i, date in enumerate(dates):
            year = date.year
            # Augmentation très forte des dotations après la départementalisation
            if year >= 2011:  # Départementalisation de Mayotte
                increase = 1 + 0.018 * (year - 2011)
            else:
                increase = 1
            
            noise = np.random.normal(1, 0.07)
            grants.append(base_grants * increase * noise)
        
        return grants
    
    def _simulate_other_revenue(self, dates):
        """Simule les autres recettes"""
        base_other = self.config["budget_base"] * 0.15  # Part plus faible
        
        other_revenue = []
        for i, date in enumerate(dates):
            growth = 1 + 0.032 * i
            noise = np.random.normal(1, 0.12)  # Plus de volatilité
            other_revenue.append(base_other * growth * noise)
        
        return other_revenue
    
    def _simulate_total_expenses(self, dates):
        """Simule les dépenses totales"""
        base_expenses = self.config["budget_base"] * 0.98  # Dépenses très proches des recettes
        
        expenses = []
        for i, date in enumerate(dates):
            growth = 1 + 0.048 * i  # Croissance très forte
            noise = np.random.normal(1, 0.08)
            expenses.append(base_expenses * growth * noise)
        
        return expenses
    
    def _simulate_operating_expenses(self, dates):
        """Simule les dépenses de fonctionnement"""
        base_operating = self.config["budget_base"] * 0.68  # Part très importante du fonctionnement
        
        operating = []
        for i, date in enumerate(dates):
            growth = 1 + 0.045 * i  # Croissance très forte
            noise = np.random.normal(1, 0.07)
            operating.append(base_operating * growth * noise)
        
        return operating
    
    def _simulate_investment_expenses(self, dates):
        """Simule les dépenses d'investissement"""
        base_investment = self.config["budget_base"] * 0.30  # Part plus faible
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            # Plans d'investissement importants après la départementalisation
            if year in [2012, 2015, 2019, 2023]:
                multiplier = 1.9
            elif year in [2009, 2014, 2021]:
                multiplier = 0.8
            else:
                multiplier = 1.0
            
            growth = 1 + 0.035 * i
            noise = np.random.normal(1, 0.20)  # Plus de volatilité
            investment.append(base_investment * growth * multiplier * noise)
        
        return investment
    
    def _simulate_debt_charges(self, dates):
        """Simule les charges de la dette"""
        base_debt_charge = self.config["budget_base"] * 0.08  # Charges de dette plus importantes
        
        debt_charges = []
        for i, date in enumerate(dates):
            year = date.year
            if year >= 2011:
                increase = 1 + 0.012 * (year - 2011)  # Augmentation plus forte après départementalisation
            else:
                increase = 1
            
            noise = np.random.normal(1, 0.13)  # Plus de volatilité
            debt_charges.append(base_debt_charge * increase * noise)
        
        return debt_charges
    
    def _simulate_staff_costs(self, dates):
        """Simule les dépenses de personnel"""
        base_staff = self.config["budget_base"] * 0.48  # Part très importante du personnel
        
        staff_costs = []
        for i, date in enumerate(dates):
            growth = 1 + 0.042 * i  # Croissance très forte
            noise = np.random.normal(1, 0.06)
            staff_costs.append(base_staff * growth * noise)
        
        return staff_costs
    
    def _simulate_gross_savings(self, dates):
        """Simule l'épargne brute"""
        savings = []
        for i, date in enumerate(dates):
            base_saving = self.config["budget_base"] * 0.02  # Épargne très faible
            
            year = date.year
            if year >= 2011:
                improvement = 1 + 0.006 * (year - 2011)  # Amélioration très lente
            else:
                improvement = 1
            
            noise = np.random.normal(1, 0.18)  # Plus de volatilité
            savings.append(base_saving * improvement * noise)
        
        return savings
    
    def _simulate_total_debt(self, dates):
        """Simule la dette totale"""
        base_debt = self.config["budget_base"] * 0.90  # Dette très importante
        
        debt = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2012, 2015, 2019, 2023]:
                change = 1.3  # Augmentation très forte
            elif year in [2009, 2014, 2021]:
                change = 0.95  # Réduction plus faible
            else:
                change = 1.0
            
            noise = np.random.normal(1, 0.12)  # Plus de volatilité
            debt.append(base_debt * change * noise)
        
        return debt
    
    def _simulate_debt_ratio(self, dates):
        """Simule le taux d'endettement"""
        ratios = []
        for i, date in enumerate(dates):
            base_ratio = 0.82  # Endettement initial très élevé
            
            year = date.year
            if year >= 2011:
                improvement = 1 - 0.008 * (year - 2011)  # Amélioration très lente
            else:
                improvement = 1
            
            noise = np.random.normal(1, 0.09)
            ratios.append(base_ratio * improvement * noise)
        
        return ratios
    
    def _simulate_tax_rate(self, dates):
        """Simule le taux de fiscalité (moyen)"""
        rates = []
        for i, date in enumerate(dates):
            base_rate = 0.75  # Fiscalité initiale très faible
            
            year = date.year
            if year >= 2011:
                increase = 1 + 0.006 * (year - 2011)  # Augmentation très lente
            else:
                increase = 1
            
            noise = np.random.normal(1, 0.05)
            rates.append(base_rate * increase * noise)
        
        return rates
    
    def _simulate_agriculture_investment(self, dates):
        """Simule l'investissement agricole"""
        base_investment = self.config["budget_base"] * 0.07  # Part plus importante
        
        # Ajustement selon les spécialités
        multiplier = 1.4 if "agriculture" in self.config["specialites"] else 0.9
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2005, 2010, 2015, 2020]:
                year_multiplier = 2.1  # Plans d'investissement très importants
            else:
                year_multiplier = 1.0
            
            growth = 1 + 0.038 * i  # Croissance très forte
            noise = np.random.normal(1, 0.18)
            investment.append(base_investment * growth * year_multiplier * multiplier * noise)
        
        return investment
    
    def _simulate_fishing_investment(self, dates):
        """Simule l'investissement dans la pêche (spécifique à Mayotte)"""
        base_investment = self.config["budget_base"] * 0.06
        
        # Ajustement selon les spécialités
        multiplier = 1.7 if "peche" in self.config["specialites"] else 0.8
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2007, 2013, 2019, 2024]:
                year_multiplier = 2.0
            else:
                year_multiplier = 1.0
            
            growth = 1 + 0.04 * i  # Croissance très forte
            noise = np.random.normal(1, 0.20)
            investment.append(base_investment * growth * year_multiplier * multiplier * noise)
        
        return investment
    
    def _simulate_transport_investment(self, dates):
        """Simule l'investissement en transport"""
        base_investment = self.config["budget_base"] * 0.05
        
        # Ajustement selon les spécialités
        multiplier = 1.5 if "transport" in self.config["specialites"] else 1.0
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2006, 2012, 2018, 2023]:
                year_multiplier = 1.9
            else:
                year_multiplier = 1.0
            
            growth = 1 + 0.035 * i
            noise = np.random.normal(1, 0.19)
            investment.append(base_investment * growth * year_multiplier * multiplier * noise)
        
        return investment
    
    def _simulate_education_investment(self, dates):
        """Simule l'investissement éducatif"""
        base_investment = self.config["budget_base"] * 0.06  # Part plus importante
        
        # Ajustement selon les spécialités
        multiplier = 1.5 if "education" in self.config["specialites"] else 1.0
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2008, 2014, 2020]:
                year_multiplier = 1.8
            else:
                year_multiplier = 1.0
            
            growth = 1 + 0.036 * i
            noise = np.random.normal(1, 0.22)  # Plus de volatilité
            investment.append(base_investment * growth * year_multiplier * multiplier * noise)
        
        return investment
    
    def _simulate_health_investment(self, dates):
        """Simule l'investissement en santé (spécifique à Mayotte)"""
        base_investment = self.config["budget_base"] * 0.05
        
        # Ajustement selon les spécialités
        multiplier = 1.6 if "sante" in self.config["specialites"] else 0.9
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2009, 2015, 2021]:
                year_multiplier = 2.1  # Plans très importants pour la santé
            else:
                year_multiplier = 1.0
            
            growth = 1 + 0.038 * i
            noise = np.random.normal(1, 0.21)
            investment.append(base_investment * growth * year_multiplier * multiplier * noise)
        
        return investment
    
    def _simulate_environment_investment(self, dates):
        """Simule l'investissement environnemental"""
        base_investment = self.config["budget_base"] * 0.04  # Part plus importante
        
        # Ajustement selon les spécialités
        multiplier = 1.6 if "environnement" in self.config["specialites"] else 0.9
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2009, 2015, 2021]:
                year_multiplier = 2.2  # Plans très importants pour l'environnement
            else:
                year_multiplier = 1.0
            
            growth = 1 + 0.04 * i
            noise = np.random.normal(1, 0.23)
            investment.append(base_investment * growth * year_multiplier * multiplier * noise)
        
        return investment
    
    def _add_municipal_trends(self, df):
        """Ajoute des tendances municipales réalistes adaptées à Mayotte"""
        for i, row in df.iterrows():
            year = row['Annee']
            
            # Développement initial (2002-2005)
            if 2002 <= year <= 2005:
                df.loc[i, 'Investissement_Agriculture'] *= 1.6
                df.loc[i, 'Investissement_Peche'] *= 1.5
            
            # Préparation à la départementalisation (2006-2010)
            if 2006 <= year <= 2010:
                df.loc[i, 'Dotations_Etat'] *= 1.25
                df.loc[i, 'Investissement'] *= 1.3
            
            # Départementalisation de Mayotte (2011)
            if year == 2011:
                df.loc[i, 'Dotations_Etat'] *= 1.8  # Forte augmentation des dotations
                df.loc[i, 'Investissement_Education'] *= 1.6
                df.loc[i, 'Investissement_Sante'] *= 1.7
            
            # Développement post-départementalisation (2012-2015)
            elif 2012 <= year <= 2015:
                df.loc[i, 'Investissement_Transport'] *= 1.5
                df.loc[i, 'Investissement_Environnement'] *= 1.4
            
            # Impact de la crise COVID-19 (2020-2021)
            if 2020 <= year <= 2021:
                if year == 2020:
                    # Baisse des recettes mais soutien de l'État
                    df.loc[i, 'Autres_Recettes'] *= 0.68
                    df.loc[i, 'Dotations_Etat'] *= 1.25
            
            # Plan de relance post-COVID spécifique à Mayotte (2022-2025)
            if year >= 2022:
                df.loc[i, 'Investissement'] *= 1.18
                df.loc[i, 'Investissement_Sante'] *= 1.22
                df.loc[i, 'Investissement_Agriculture'] *= 1.15
    
    def create_financial_analysis(self, df):
        """Crée une analyse complète des finances communales"""
        plt.style.use('seaborn-v0_8')
        fig = plt.figure(figsize=(20, 24))
        
        # 1. Évolution des recettes et dépenses
        ax1 = plt.subplot(4, 2, 1)
        self._plot_revenue_expenses(df, ax1)
        
        # 2. Structure des recettes
        ax2 = plt.subplot(4, 2, 2)
        self._plot_revenue_structure(df, ax2)
        
        # 3. Structure des dépenses
        ax3 = plt.subplot(4, 2, 3)
        self._plot_expenses_structure(df, ax3)
        
        # 4. Investissements communaux
        ax4 = plt.subplot(4, 2, 4)
        self._plot_investments(df, ax4)
        
        # 5. Dette et endettement
        ax5 = plt.subplot(4, 2, 5)
        self._plot_debt(df, ax5)
        
        # 6. Indicateurs de performance
        ax6 = plt.subplot(4, 2, 6)
        self._plot_performance_indicators(df, ax6)
        
        # 7. Démographie
        ax7 = plt.subplot(4, 2, 7)
        self._plot_demography(df, ax7)
        
        # 8. Investissements sectoriels
        ax8 = plt.subplot(4, 2, 8)
        self._plot_sectorial_investments(df, ax8)
        
        plt.suptitle(f'Analyse des Comptes Communaux de {self.commune} - Mayotte ({self.start_year}-{self.end_year})', 
                    fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig(f'{self.commune}_financial_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Générer les insights
        self._generate_financial_insights(df)
    
    def _plot_revenue_expenses(self, df, ax):
        """Plot de l'évolution des recettes et dépenses"""
        ax.plot(df['Annee'], df['Recettes_Totales'], label='Recettes Totales', 
               linewidth=2, color='#2A9D8F', alpha=0.8)
        ax.plot(df['Annee'], df['Depenses_Totales'], label='Dépenses Totales', 
               linewidth=2, color='#E76F51', alpha=0.8)
        
        ax.set_title('Évolution des Recettes et Dépenses (M€)', 
                    fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    def _plot_revenue_structure(self, df, ax):
        """Plot de la structure des recettes"""
        years = df['Annee']
        width = 0.8
        
        bottom = np.zeros(len(years))
        categories = ['Impots_Locaux', 'Dotations_Etat', 'Autres_Recettes']
        colors = ['#264653', '#2A9D8F', '#E76F51']
        labels = ['Impôts Locaux', 'Dotations État', 'Autres Recettes']
        
        for i, category in enumerate(categories):
            ax.bar(years, df[category], width, label=labels[i], bottom=bottom, color=colors[i])
            bottom += df[category]
        
        ax.set_title('Structure des Recettes (M€)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
    
    def _plot_expenses_structure(self, df, ax):
        """Plot de la structure des dépenses"""
        years = df['Annee']
        width = 0.8
        
        bottom = np.zeros(len(years))
        categories = ['Fonctionnement', 'Investissement', 'Charge_Dette', 'Personnel']
        colors = ['#264653', '#2A9D8F', '#E76F51', '#F9A602']
        labels = ['Fonctionnement', 'Investissement', 'Charge Dette', 'Personnel']
        
        for i, category in enumerate(categories):
            ax.bar(years, df[category], width, label=labels[i], bottom=bottom, color=colors[i])
            bottom += df[category]
        
        ax.set_title('Structure des Dépenses (M€)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
    
    def _plot_investments(self, df, ax):
        """Plot des investissements communaux"""
        ax.plot(df['Annee'], df['Investissement_Agriculture'], label='Agriculture', 
               linewidth=2, color='#264653', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Peche'], label='Pêche', 
               linewidth=2, color='#2A9D8F', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Transport'], label='Transport', 
               linewidth=2, color='#E76F51', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Education'], label='Éducation', 
               linewidth=2, color='#F9A602', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Sante'], label='Santé', 
               linewidth=2, color='#6A0572', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Environnement'], label='Environnement', 
               linewidth=2, color='#45B7D1', alpha=0.8)
        
        ax.set_title('Répartition des Investissements (M€)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    def _plot_debt(self, df, ax):
        """Plot de la dette et du taux d'endettement"""
        # Dette totale
        ax.bar(df['Annee'], df['Dette_Totale'], label='Dette Totale (M€)', 
              color='#264653', alpha=0.7)
        
        ax.set_title('Dette Communale et Taux d\'Endettement', fontsize=12, fontweight='bold')
        ax.set_ylabel('Dette (M€)', color='#264653')
        ax.tick_params(axis='y', labelcolor='#264653')
        ax.grid(True, alpha=0.3, axis='y')
        
        # Taux d'endettement en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Taux_Endettement'], label='Taux d\'Endettement', 
                linewidth=3, color='#E76F51')
        ax2.set_ylabel('Taux d\'Endettement', color='#E76F51')
        ax2.tick_params(axis='y', labelcolor='#E76F51')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    def _plot_performance_indicators(self, df, ax):
        """Plot des indicateurs de performance"""
        # Épargne brute
        ax.bar(df['Annee'], df['Epargne_Brute'], label='Épargne Brute (M€)', 
              color='#2A9D8F', alpha=0.7)
        
        ax.set_title('Indicateurs de Performance', fontsize=12, fontweight='bold')
        ax.set_ylabel('Épargne Brute (M€)', color='#2A9D8F')
        ax.tick_params(axis='y', labelcolor='#2A9D8F')
        ax.grid(True, alpha=0.3, axis='y')
        
        # Taux de fiscalité en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Taux_Fiscalite'], label='Taux de Fiscalité', 
                linewidth=3, color='#F9A602')
        ax2.set_ylabel('Taux de Fiscalité', color='#F9A602')
        ax2.tick_params(axis='y', labelcolor='#F9A602')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    def _plot_demography(self, df, ax):
        """Plot de l'évolution démographique"""
        ax.plot(df['Annee'], df['Population'], label='Population', 
               linewidth=2, color='#264653', alpha=0.8)
        
        ax.set_title('Évolution Démographique', fontsize=12, fontweight='bold')
        ax.set_ylabel('Population', color='#264653')
        ax.tick_params(axis='y', labelcolor='#264653')
        ax.grid(True, alpha=0.3)
        
        # Nombre de ménages en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Menages'], label='Ménages', 
                linewidth=2, color='#E76F51', alpha=0.8)
        ax2.set_ylabel('Ménages', color='#E76F51')
        ax2.tick_params(axis='y', labelcolor='#E76F51')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    def _plot_sectorial_investments(self, df, ax):
        """Plot des investissements sectoriels"""
        years = df['Annee']
        width = 0.8
        
        bottom = np.zeros(len(years))
        categories = ['Investissement_Agriculture', 'Investissement_Peche', 
                     'Investissement_Transport', 'Investissement_Education', 
                     'Investissement_Sante', 'Investissement_Environnement']
        colors = ['#264653', '#2A9D8F', '#E76F51', '#F9A602', '#6A0572', '#45B7D1']
        labels = ['Agriculture', 'Pêche', 'Transport', 'Éducation', 'Santé', 'Environnement']
        
        for i, category in enumerate(categories):
            ax.bar(years, df[category], width, label=labels[i], bottom=bottom, color=colors[i])
            bottom += df[category]
        
        ax.set_title('Répartition Sectorielle des Investissements (M€)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
    
    def _generate_financial_insights(self, df):
        """Génère des insights analytiques adaptés à Mayotte"""
        print(f"🏛️ INSIGHTS ANALYTIQUES - Commune de {self.commune} (Mayotte)")
        print("=" * 60)
        
        # 1. Statistiques de base
        print("\n1. 📈 STATISTIQUES GÉNÉRALES:")
        avg_revenue = df['Recettes_Totales'].mean()
        avg_expenses = df['Depenses_Totales'].mean()
        avg_savings = df['Epargne_Brute'].mean()
        avg_debt = df['Dette_Totale'].mean()
        
        print(f"Recettes moyennes annuelles: {avg_revenue:.2f} M€")
        print(f"Dépenses moyennes annuelles: {avg_expenses:.2f} M€")
        print(f"Épargne brute moyenne: {avg_savings:.2f} M€")
        print(f"Dette moyenne: {avg_debt:.2f} M€")
        
        # 2. Croissance (très forte à Mayotte)
        print("\n2. 📊 TAUX DE CROISSANCE:")
        revenue_growth = ((df['Recettes_Totales'].iloc[-1] / 
                          df['Recettes_Totales'].iloc[0]) - 1) * 100
        population_growth = ((df['Population'].iloc[-1] / 
                             df['Population'].iloc[0]) - 1) * 100
        
        print(f"Croissance des recettes ({self.start_year}-{self.end_year}): {revenue_growth:.1f}%")
        print(f"Croissance de la population ({self.start_year}-{self.end_year}): {population_growth:.1f}%")
        
        # 3. Structure financière (spécificités mahoraises)
        print("\n3. 📋 STRUCTURE FINANCIÈRE:")
        tax_share = (df['Impots_Locaux'].mean() / df['Recettes_Totales'].mean()) * 100
        state_share = (df['Dotations_Etat'].mean() / df['Recettes_Totales'].mean()) * 100
        investment_share = (df['Investissement'].mean() / df['Depenses_Totales'].mean()) * 100
        
        print(f"Part des impôts locaux dans les recettes: {tax_share:.1f}%")
        print(f"Part des dotations de l'État dans les recettes: {state_share:.1f}%")
        print(f"Part de l'investissement dans les dépenses: {investment_share:.1f}%")
        
        # 4. Dette et fiscalité
        print("\n4. 💰 ENDETTEMENT ET FISCALITÉ:")
        avg_debt_ratio = df['Taux_Endettement'].mean() * 100
        avg_tax_rate = df['Taux_Fiscalite'].mean()
        last_debt_ratio = df['Taux_Endettement'].iloc[-1] * 100
        
        print(f"Taux d'endettement moyen: {avg_debt_ratio:.1f}%")
        print(f"Taux d'endettement final: {last_debt_ratio:.1f}%")
        print(f"Taux de fiscalité moyen: {avg_tax_rate:.2f}")
        
        # 5. Spécificités de la commune mahoraise
        print(f"\n5. 🌟 SPÉCIFICITÉS DE {self.commune.upper()} (MAYOTTE):")
        print(f"Type de commune: {self.config['type']}")
        print(f"Spécialités: {', '.join(self.config['specialites'])}")
        
        # 6. Événements marquants spécifiques à Mayotte
        print("\n6. 📅 ÉVÉNEMENTS MARQUANTS MAYOTTE:")
        print("• 2002-2005: Développement initial et renforcement des infrastructures")
        print("• 2006-2010: Préparation à la départementalisation")
        print("• 2011: Départementalisation de Mayotte et augmentation des dotations")
        print("• 2012-2015: Développement des services publics et des infrastructures")
        print("• 2018: Mouvements sociaux et renforcement des investissements")
        print("• 2020-2021: Impact de la crise COVID-19 et plans de soutien")
        print("• 2022-2025: Plan de relance post-COVID spécifique à Mayotte")
        
        # 7. Recommandations adaptées à Mayotte
        print("\n7. 💡 RECOMMANDATIONS STRATÉGIQUES:")
        if "peche" in self.config["specialites"]:
            print("• Moderniser la pêche artisanale et développer l'aquaculture")
            print("• Valoriser les produits de la pêche locale")
        if "agriculture" in self.config["specialites"]:
            print("• Développer l'agriculture vivrière et les filières locales")
            print("• Moderniser les techniques agricoles et l'irrigation")
        if "tourisme" in self.config["specialites"]:
            print("• Développer l'écotourisme et le tourisme responsable")
            print("• Valoriser les atouts naturels (lagons, plages, biodiversité)")
        print("• Améliorer les infrastructures de transport et de mobilité")
        print("• Renforcer les services publics (santé, éducation, eau)")
        print("• Lutter contre l'habitat informel et développer le logement social")
        print("• Préserver l'environnement et la biodiversité exceptionnelle")

def main():
    """Fonction principale pour Mayotte"""
    # Liste des communes de Mayotte
    communes = [
        "Dzaoudzi", "Pamandzi", "Mamoudzou", "Dembeni", "Bandrélé", 
        "Kani-Kéli", "Bouéni", "Chirongui", "Sada", "Ouangani", 
        "Chiconi", "Tsingoni", "M'Tsangamouji", "Acoua", "Mtsamboro", 
        "Bandraboua", "Koungou"
    ]
    
    print("🏛️ ANALYSE DES COMPTES COMMUNAUX DE MAYOTTE (2002-2025)")
    print("=" * 60)
    
    # Demander à l'utilisateur de choisire une commune
    print("Liste des communes disponibles:")
    for i, commune in enumerate(communes, 1):
        print(f"{i}. {commune}")
    
    try:
        choix = int(input("\nChoisissez le numéro de la commune à analyser: "))
        if choix < 1 or choix > len(communes):
            raise ValueError
        commune_selectionnee = communes[choix-1]
    except (ValueError, IndexError):
        print("Choix invalide. Sélection de Mamoudzou par défaut.")
        commune_selectionnee = "Mamoudzou"
    
    # Initialiser l'analyseur
    analyzer = MayotteCommuneFinanceAnalyzer(commune_selectionnee)
    
    # Générer les données
    financial_data = analyzer.generate_financial_data()
    
    # Sauvegarder les données
    output_file = f'{commune_selectionnee}_financial_data_2002_2025.csv'
    financial_data.to_csv(output_file, index=False)
    print(f"💾 Données sauvegardées: {output_file}")
    
    # Aperçu des données
    print("\n👀 Aperçu des données:")
    print(financial_data[['Annee', 'Population', 'Recettes_Totales', 'Depenses_Totales', 'Dette_Totale']].head())
    
    # Créer l'analyse
    print("\n📈 Création de l'analyse financière...")
    analyzer.create_financial_analysis(financial_data)
    
    print(f"\n✅ Analyse des comptes communaux de {commune_selectionnee} terminée!")
    print(f"📊 Période: {analyzer.start_year}-{analyzer.end_year}")
    print("📦 Données: Démographie, finances, investissements, dette")

if __name__ == "__main__":
    main()