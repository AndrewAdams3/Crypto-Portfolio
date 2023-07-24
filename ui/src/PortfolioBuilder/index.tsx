import { useEffect, useState } from "react";
import { CurrencyTile } from "../CurrencyTile";
import * as classes from './styles.module.css';
import { Metrics } from "../Metrics";

export type PortfolioBuilderInput = {
    portfolio: {
        portfolio: {
            id?: number;
            userId: number;
        }
        currencies: any[]
    }
    userId: number;
    onCreatePortfolio: () => Promise<void>;
    hasPortfolio: boolean;
}

export function PortfolioBuilder({portfolio, userId, onCreatePortfolio, hasPortfolio}: PortfolioBuilderInput) {
    const [availableCurrencies, setAvailableCurrencies] = useState<any[]>([]);
    const [activeCurrencies, setActiveCurrencies] = useState<any[]>(portfolio.currencies ?? []);
    const [showMetrics, setShowMetrics] = useState(false);

    useEffect(() => {
        fetch("http://localhost:8000/currency/")
            .then((response) => response.json())
            .then((data) => setAvailableCurrencies(data));
    }, [])

    const addCurrency = async (currency: any) => {
        if(hasPortfolio) {
            await fetch(`http://localhost:8000/portfolio/${portfolio.portfolio.id}/currencies/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    currencyId: currency.id
                })
            })
        }
        
        setActiveCurrencies((actives) => [...actives, currency])
    }
    
    const removeCurrency = async (currency: any) => {
        if(hasPortfolio) {
            if(activeCurrencies.length === 5) {
                alert("You must have at least 5 currencies in your portfolio")
                return;
            }

            await fetch(`http://localhost:8000/portfolio/${portfolio.portfolio.id}/currencies/`, {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    currencyId: currency.id
                })
            })
        }
        setActiveCurrencies((actives) => actives.filter(a => a.id !== currency.id))
    }

    const createPortfolio = async () => {
        if(activeCurrencies.length < 5) {
            alert("You must have at least 5 currencies in your portfolio")
            return;
        }

        await fetch("http://localhost:8000/portfolio/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ 
                portfolio: { userId: userId }, 
                currencies: activeCurrencies.map(c => ({
                    currencyId: c.id
                })) 
            })
        })
        await onCreatePortfolio();
    }

    const viewMetrics = (value: boolean) => {
        setShowMetrics(value)
    }
    
    return (<>
        <div className={classes.container}>
            <div style={{flex: 1}}>
                <span className={classes.portfolio_title}>
                    <h1>
                        Portfolio
                    </h1>
                    <button onClick={() => viewMetrics(true)}>View Metrics</button>
                </span>
                {
                    activeCurrencies
                    .sort((a, b) => a.name.localeCompare(b.name))
                    .map(c => <CurrencyTile key={`active-${c.id}`} buttonText="Remove from Portfolio" click={() => removeCurrency(c)} name={c.name} />)
                } 
            </div>
            <div style={{flex: 1}}>
                <h1>Available Currencies</h1>
                {
                    availableCurrencies
                    .filter(c => !activeCurrencies.find(ac => ac.id === c.id))
                    .sort((a, b) => a.name.localeCompare(b.name))
                    .map(c => <CurrencyTile key={`available-${c.id}`} buttonText="Add To Portfolio" click={() => addCurrency(c)} name={c.name}/>)
                }
            </div>
        </div>
        {
            !hasPortfolio && 
            <div>    
                <button onClick={createPortfolio}>Create New Portfolio</button>
            </div>
        }
        {
            showMetrics && <Metrics userId={userId} onClose={() => viewMetrics(false)}/>
        }
    </>);
}