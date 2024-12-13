import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { NgxChartsModule, Color, ScaleType } from '@swimlane/ngx-charts';

@Component({
  selector: 'app-chart',
  standalone: true,
  imports: [NgxChartsModule],
  templateUrl: './chart.component.html',
  styleUrls: ['./chart.component.css']
})
export class ChartComponent implements OnInit {
  chartData: any[] = [];
  colorScheme: Color = {
    domain: ['#5AA454', '#A10A28', '#C7B42C', '#AAAAAA'],
    name: 'custom',
    selectable: true,
    group: ScaleType.Ordinal, // Utilisez ScaleType.Ordinal ici
  };

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.loadChartData();
  }

  loadChartData(): void {
    this.http.get<any[]>('http://127.0.0.1:5000/searches/all')
      .subscribe(data => {
        this.chartData = this.processData(data);
      });
  }

  processData(data: any[]): any[] {
    const counts = data.reduce((acc, search) => {
      acc[search.algorithm] = (acc[search.algorithm] || 0) + 1;
      return acc;
    }, {});
    return Object.keys(counts).map(key => ({ name: key, value: counts[key] }));
  }
}
