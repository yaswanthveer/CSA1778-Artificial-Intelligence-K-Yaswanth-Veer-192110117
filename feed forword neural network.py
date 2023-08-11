import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Initialize weights and biases
        self.weights_input_hidden = np.random.rand(self.input_size, self.hidden_size)
        self.bias_hidden = np.zeros((1, self.hidden_size))
        self.weights_hidden_output = np.random.rand(self.hidden_size, self.output_size)
        self.bias_output = np.zeros((1, self.output_size))
        
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(self, x):
        return x * (1 - x)
    
    def forward(self, X):
        self.hidden_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = self.sigmoid(self.hidden_input)
        self.output = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        return self.sigmoid(self.output)
    
    def backward(self, X, y, output):
        self.output_error = y - output
        self.output_delta = self.output_error * self.sigmoid_derivative(output)
        
        self.hidden_error = self.output_delta.dot(self.weights_hidden_output.T)
        self.hidden_delta = self.hidden_error * self.sigmoid_derivative(self.hidden_output)
        
        self.weights_hidden_output += self.hidden_output.T.dot(self.output_delta)
        self.bias_output += np.sum(self.output_delta, axis=0, keepdims=True)
        
        self.weights_input_hidden += X.T.dot(self.hidden_delta)
        self.bias_hidden += np.sum(self.hidden_delta, axis=0)
        
    def train(self, X, y, epochs):
        for epoch in range(epochs):
            output = self.forward(X)
            self.backward(X, y, output)
            
            if (epoch + 1) % 1000 == 0:
                loss = np.mean(np.square(y - output))
                print(f"Epoch {epoch+1}/{epochs}, Loss: {loss:.4f}")
                
    def predict(self, X):
        return np.round(self.forward(X))
    

if __name__ == "__main__":
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])
    
    input_size = X.shape[1]
    hidden_size = 4
    output_size = y.shape[1]
    
    nn = NeuralNetwork(input_size, hidden_size, output_size)
    
    epochs = 10000
    nn.train(X, y, epochs)
    
    predictions = nn.predict(X)
    print("Predictions:")
    print(predictions)