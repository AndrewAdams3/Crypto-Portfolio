import { useContext, useState } from "react";
import { CurrencyTile } from "../CurrencyTile";
import * as classes from './styles.module.css';
import { Metrics } from "../Metrics";
import { PortfolioDetails } from "../types";
import { AppContext } from "../Context";

export type PortfolioBuilderInput = {
    portfolio: PortfolioDetails;
    userId: number;
    onCreatePortfolio: () => Promise<void>;
    hasPortfolio: boolean;
}

export function PortfolioBuilder({portfolio, userId, onCreatePortfolio, hasPortfolio}: PortfolioBuilderInput) {
    const [showMetrics, setShowMetrics] = useState(false);
    const { addRemoveCurrency, availableCurrencies } = useContext(AppContext);
    
    const createPortfolio = async () => {
        if(portfolio.currencies.length < 5) {
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
                currencies: portfolio.currencies.map(c => ({
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
                <div className={classes.portfolio_title}>
                    <h1>
                        Portfolio
                    </h1>
                    <button onClick={() => viewMetrics(true)}>View Metrics</button>
                </div>
                {
                    portfolio.currencies
                    .sort((a, b) => a.name.localeCompare(b.name))
                    .map(c => <CurrencyTile key={`active-${c.id}`} buttonText="Remove from Portfolio" click={() => addRemoveCurrency(c, false)} name={c.name} />)
                } 
            </div>
            <div style={{flex: 1}}>
                <div className={classes.portfolio_title}>
                    <h1>Available Currencies</h1>
                </div>
                {
                    availableCurrencies
                    .filter(c => !portfolio.currencies.find(ac => ac.id === c.id))
                    .sort((a, b) => a.name.localeCompare(b.name))
                    .map(c => <CurrencyTile key={`available-${c.id}`} buttonText="Add To Portfolio" click={() => addRemoveCurrency(c, true)} name={c.name}/>)
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
            showMetrics && <Metrics portfolioId={portfolio.portfolio.id!} onClose={() => viewMetrics(false)}/>
        }
    </>);
}
