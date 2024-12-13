import { Routes } from '@angular/router';
import { HomepageComponent } from './homepage/homepage.component';
import { ChartPageComponent } from './chart-page/chart-page.component';

export const routes: Routes = [
  {
    path: '',
    component: HomepageComponent,
  },
  {
    path: 'dashboard',
    component: ChartPageComponent,
  },
];
