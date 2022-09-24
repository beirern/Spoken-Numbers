import { Component } from 'react';

class Core extends Component {
  constructor(props) {
    super(props);
    this.state = { time: 0 };

    this.handleTimeChange = this.handleTimeChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleTimeChange(event) {
    this.setState({ time: event.target.value })
  }

  handleSubmit(event) {
    alert('Time: ' + this.state.time)
  }

  render() {
    return (
      <div>
        <header>
          <h1>Core</h1>
        </header>
        <form onSubmit={this.handleSubmit}>
          <label>
            Seconds to Go:
            <input type="number" value={this.state.value}
            onChange={this.handleTimeChange} />
          </label>
          <input type="submit" value="Go!" />
        </form>
      </div>
    );
  }
}

export default Core;
