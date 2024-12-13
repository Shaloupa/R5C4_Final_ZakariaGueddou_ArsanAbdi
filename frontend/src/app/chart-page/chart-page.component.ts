import { Component } from '@angular/core';
import jsonData from '../../assets/space_travel_data.json';
import {
  BarChartModule,
  LineChartModule,
  NumberCardModule,
  PieChartModule,
} from '@swimlane/ngx-charts';
import { RouterOutlet } from '@angular/router';

/**
 * Je définis ces données uniquement pour vous.
 *
 * Tous les objets du json contiennent ces données
 **/
type DataFromJson = {
  company: string;
  destination: string;
  price: number;
  date: string;
  rate: number;
  motive: string;
  satisfied: boolean;
  gender: 'M' | 'F' | 'N/A';
  shipType: string;
  travelClass: 'eco' | 'premios' | 'business';
  isMember: boolean;
}[];

type SingleData = {
  value: number;
  name: string;
}[];

type MultipleData = {
  name: string;
  series: SingleData;
}[];

/**
 * Pour les graphiques acceptant un seul jeu de données, si vous appelez cette fonction
 * avec un objet, elle le transformera en un tableau où chaque objet aura deux propriétés.
 *
 * Une propriété name représentant la clé et propriété value représentant une valeur.
 *
 * @example
 * ```ts
 * toSingleData({ a: 1, b: 2 }) -> [{ name: 'a', value: 1 }, { name: 'b', value: 2 }]
 * toSingleData({ satisfied: 10, unsatisfied: 20 }) -> [{ name: 'satisfied', value: 10 }, { name: 'unsatisfied', value: 20 }]
 * ```
 */
function toSingleData(data: Record<string, number>): SingleData {
  return Object.entries(data).map(([name, value]) => ({ name, value }));
}

/**
 *  Pour les graphiques acceptant plusieurs jeux de données
 *
 *  @example
 * ```ts
 * toMultipleData('Vaisseau 1', { satisfied: 1500, unsatisfied: 2500 }) -> [{ name: 'Vaisseau 1', series: [{ name: 'satisfied', value: 1500 }, { name: 'unsatisfied', value: 2500 }] }]
 * ```
 */
function toMultipleData(serie: string, data: any): MultipleData {
  return [
    {
      name: serie,
      series: toSingleData(data),
    },
  ];
}

@Component({
  selector: 'app-chart-page',
  standalone: true,
  imports: [NumberCardModule, BarChartModule, PieChartModule],
  templateUrl: './chart-page.component.html',
  styleUrl: './chart-page.component.css',
})
export class ChartPageComponent {
  
  nbVoyages: number = 0;
  voyage_eco: number = 0;
  voyage_premios: number = 0;
  voyage_business: number = 0;
  prixMoyen: number = 0;
  prixMoyen_eco: number = 0;
  prixMoyen_premios: number = 0;
  prixMoyen_business: number = 0;
  avisMoyen: number = 0;
  avisMoyen_eco: number = 0;
  avisMoyen_premios: number = 0;
  avisMoyen_business: number = 0;

  indicatorsDataExo2NbVoyages: SingleData = [];
  indicatorsDataExo2Prix: SingleData = [];
  indicatorsDataExo2Avis: SingleData = [];
  indicatorsDataExo3: SingleData = [];
  motifsInsatisfaction: SingleData = [];

  notesNegatives() {
    return jsonData.filter(x => x.rate <= 2);
  }

  ngOnInit() {
    this.nbVoyages = jsonData.length;
    this.voyage_eco = jsonData.filter(x => x.travelClass === 'eco').length;
    this.voyage_premios = jsonData.filter(x => x.travelClass === 'premios').length;
    this.voyage_business = jsonData.filter(x => x.travelClass === 'business').length;
    this.prixMoyen = (jsonData.reduce((sommeprix, x) => sommeprix + x.price,0) / this.nbVoyages);
    this.prixMoyen_eco = (jsonData.filter(x => x.travelClass === 'eco').reduce((sommeprix, x) => sommeprix + x.price,0) / this.voyage_eco);
    this.prixMoyen_premios = (jsonData.filter(x => x.travelClass === 'premios').reduce((sommeprix, x) => sommeprix + x.price,0) / this.voyage_premios);
    this.prixMoyen_business = (jsonData.filter(x => x.travelClass === 'business').reduce((sommeprix, x) => sommeprix + x.price,0) / this.voyage_business);
    this.avisMoyen = (jsonData.reduce((sommeavis, x) => sommeavis + x.rate,0) / this.nbVoyages);
    this.avisMoyen_eco = (jsonData.filter(x => x.travelClass === 'eco').reduce((sommeavis, x) => sommeavis + x.rate,0) / this.voyage_eco);
    this.avisMoyen_premios = (jsonData.filter(x => x.travelClass === 'premios').reduce((sommeavis, x) => sommeavis + x.rate,0) / this.voyage_premios);
    this.avisMoyen_business = (jsonData.filter(x => x.travelClass === 'business').reduce((sommeavis, x) => sommeavis + x.rate,0) / this.voyage_business);
    this.calculerMotifsInsatisfaction();
  
    const donnees_exo_2_voyage = {
      nombre_de_voyages : this.nbVoyages,
      nombre_de_voyages_eco : this.voyage_eco,
      nombre_de_voyages_premios : this.voyage_premios,
      nombre_de_voyages_business : this.voyage_business,
    };

    const donnees_exo_2_prix = {
      moyenne_prix : this.prixMoyen,
      moyenne_prix_eco : this.prixMoyen_eco,
      moyenne_prix_premios : this.prixMoyen_premios,
      moyenne_prix_business : this.prixMoyen_business,
    };
      
    const donnees_exo_2_avis = {
      moyenne_avis : this.avisMoyen,
      moyenne_avis_eco : this.avisMoyen_eco,
      moyenne_avis_premios : this.avisMoyen_premios,
      moyenne_avis_business : this.avisMoyen_business,
    };

    this.indicatorsDataExo2NbVoyages = toSingleData(donnees_exo_2_voyage);
    this.indicatorsDataExo2Prix = toSingleData(donnees_exo_2_prix);
    this.indicatorsDataExo2Avis = toSingleData(donnees_exo_2_avis);
    const motives_neg = this.notesNegatives().map(x => x.motive);
  }

  calculerMotifsInsatisfaction() {
    // Étape 1 : Filtrer les passagers avec une note négative (<= 2)
    const passagersInsatisfaits = jsonData.filter((x) => x.rate <= 2);
  
    // Étape 2 : Compter les occurrences des motifs d'insatisfaction
    const compteMotifs = passagersInsatisfaits.reduce<Record<string, number>>(
      (acc, passager) => {
        const motif = passager.motive;
        acc[motif] = (acc[motif] || 0) + 1;
        return acc;
      },
      {} // Initialisation avec un objet vide de type Record<string, number>
    );
  
    // Étape 3 : Convertir en données pour ngx-charts
    this.motifsInsatisfaction = toSingleData(compteMotifs);
  }
}
