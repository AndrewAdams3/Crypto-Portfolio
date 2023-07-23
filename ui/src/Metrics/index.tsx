import { useEffect, useMemo, useState } from "react";

type Metric = {
    id: number;
    name: string;
    marketCap: number;
    volume: number;
    price: number;
}

function MetricRow(metric: Metric) {
    return (
    <tr key={metric.id}>
        <td>{metric.name}</td>
        <td>{metric.marketCap}</td>
        <td>{metric.volume}</td>
        <td>{metric.price}</td>
    </tr>
    )
}

type MetricsProps = {
    currencies: number[];
    userId: number;
}

export function Metrics({currencies, userId}: MetricsProps) {
    const [metrics, setMetrics] = useState<Metric[]>([]);

    useEffect(() => {
        //fetch metrics
        fetch(`http://localhost:8000/portfolio/${userId}/metrics/`)
            .then((response) => response.json())
            .then((json) => setMetrics(json))
    }, []);

    const rows = useMemo(() => {
        return metrics.map((metric) => (
            <MetricRow key={metric.id} {...metric} />
        ))
    }, [metrics]);

    return (
        <div>
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Market Cap</th>
                        <th>Volume</th>
                        <th>Price</th>
                    </tr>
                </thead>
                <tbody>
                    {rows}
                </tbody>    
            </table>
        </div>
    )
}