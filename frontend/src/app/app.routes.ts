import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { ListComponent } from './list/list.component';
import { ChartComponent } from './chart/chart.component';

export const routes: Routes = [
  { path: '', component: HomeComponent }, // Page d'accueil
  { path: 'list', component: ListComponent }, // Page de liste paginée
  { path: 'chart', component: ChartComponent }, // Page graphique
  { path: '**', redirectTo: '' } // Redirection vers la page d'accueil pour les routes invalides
];
