const path = require('path');
const fs = require('fs');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const webpack = require('webpack');

module.exports = {
  entry: './src/entry.jsx',
  output: {
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, 'dist')
  },
  // devtool: 'source-map' moved to npm script.
  devServer: {
    // host: "dev.safer.lab",
    contentBase: './dist',
    port: 9000,
    https: true,
    hot: true,
    inline: true,
    historyApiFallback: true
  },
  plugins: [
    new CleanWebpackPlugin(['dist']),
    new HtmlWebpackPlugin({
      title: 'TODO-TOGO',
      inject: 'body',
      template: path.join(__dirname, 'src/template/html_base.ejs'),
      appMountId: 'bmw-app-root'
    }),
    // UglifyJS plugin is enabled by default in production mode.
  ],
  resolve: {
    extensions: [".js", ".jsx", ".json"]
  },
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        use: ['babel-loader']
      },
      { // stylesheet
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
      },
      { // less
        test: /\.less$/,
        use: ['style-loader', 'css-loader', 'less-loader']
      },
      { // image
        test: /\.(png|jpg)$/,
        use: ['file-loader']
      },
      {
        test: /\.(woff|woff2|eot|ttf|svg)$/,
        use: ['file-loader']
      }
    ]
  }
};