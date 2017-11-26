import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Route, Link } from 'react-router-dom';

import { Layout, Menu, Icon } from 'antd';
const { Header, Sider, Content } = Layout;

import AskForInputView from './view/askForInput';
import WaitingNlpResultView from './view/waitingNlpResult';
import ListAllToDoToGoView from './view/listAllToDoToGo';
import ShowPathView from './view/showPath';

export class BmwChallengeGlobalRouter extends React.Component {
    constructor() {
        super()
    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <div>
                        <div>
                            <Link to="/">askForInput</Link>
                            <Link to="/msgSent">msgSent</Link>
                            <Link to="/listGoals">listGoals</Link>
                            <Link to="/showPath">showPath</Link>
                        </div>
                        <Route exact path="/" component={AskForInputView} />
                        <Route path="/msgSent" component={WaitingNlpResultView} />
                        <Route path="/listGoals" component={ListAllToDoToGoView} />
                        <Route path="/showPath" component={ShowPathView}/>
                    </div>
                </BrowserRouter>
            </div>
        )
    }
}

ReactDOM.render(
    <BmwChallengeGlobalRouter/>,
    document.getElementById('bmw-app-root')
);
