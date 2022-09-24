import { Component } from 'react';

class Boxing extends Component {
  constructor(props) {
    super(props);
    this.state = { comboNumber: 0, time: 0 };

    this.handleComboChange = this.handleComboChange.bind(this);
    this.handleTimeChange = this.handleTimeChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleComboChange(event) {
    this.setState({ comboNumber: event.target.value })
  }

  handleTimeChange(event) {
    this.setState({ time: event.target.value })
  }

  handleSubmit(event) {
    alert('Combos: ' + this.state.comboNumber + ' Time: ' + this.state.time)
  }

  render() {
    return (
      <div>
        <header>
          <h1> Boxing </h1>
        </header>
        <form onSubmit={this.handleSubmit}>
          <label>
            Number of Punches in Combinations:
            <input type="number" value={this.state.value}
            onChange={this.handleComboChange} />
          </label>
          <label>
            Rounds to go:
            <input type="number" value={this.state.value}
            onChange={this.handleTimeChange} />
          </label>
          <input type="submit" value="Go!" />
        </form>
      </div>
    );
  }
}

export default Boxing;
