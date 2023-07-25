import { useEffect, useMemo, useState } from "react";
import * as classes from './styles.module.css';

type CurrencyMetric = {
    id: number;
    name: string;
    symbol: string;
    market_cap: number;
    volume: number;
    price: number;
    price_change_percentage_24h: number;
}

type MetricResponse = {
    currencies: CurrencyMetric[];
    totalVolume: number;
    highestTradingVolume: CurrencyMetric;
}

type MetricRowProps = {
    metric: CurrencyMetric;
    highestVolume: boolean;
}

function MetricRow({ metric, highestVolume }: MetricRowProps) {
    return (
    <tr key={metric.id} style={highestVolume ? {border: '1px solid green'} : {}}>
        <td>{metric.name}</td>
        <td>{metric.market_cap}</td>
        <td style={highestVolume ? {color: 'green'} : {}}>{metric.volume}{highestVolume ? "*" : null}</td>
        <td>{metric.price}</td>
        <td>{metric.price_change_percentage_24h}%</td>
    </tr>
    )
}

type MetricsProps = {
    portfolioId: number;
    onClose: () => void;
}

export function Metrics({portfolioId, onClose}: MetricsProps) {
    const [metrics, setMetrics] = useState<MetricResponse>();

    useEffect(() => {
        fetch(`http://localhost:8000/portfolio/${portfolioId}/metrics/`)
            .then((response) => response.json())
            .then((json: MetricResponse) => setMetrics(json))
    }, [portfolioId]);

    const rows = useMemo(() => {
        if(!metrics) return null;

        return metrics.currencies.map((metric) => (
            <MetricRow key={metric.id} metric={metric} highestVolume={metric.id === metrics.highestTradingVolume.id} />
        ))
    }, [portfolioId, metrics?.currencies, metrics?.highestTradingVolume]);

    return (
        <div className={classes.container}>
            <button className={classes.close_button} onClick={onClose}>Close</button>
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Market Cap</th>
                        <th>Volume</th>
                        <th>Price</th>
                        <th>24h Price Change</th>
                    </tr>
                </thead>
                <tbody>
                    {rows}
                </tbody>    
            </table>
            <p style={{color: 'green'}}>*Highest trading volume</p>
            <p>Total Trading Volume: {metrics?.totalVolume}</p>
        </div>
    )
}
