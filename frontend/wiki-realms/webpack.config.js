const path = require('path');

module.exports = {
	resolve: {
		fallback: {
			"fs": false,
			"path": false,
			"os": false,
			"child_process": false,
			"stream": require.resolve("stream-browserify"),
		}
	},
	entry: './src/index.js',
	output: {
		filename: 'bundle.js',
		path: path.resolve(__dirname, 'dist'),
	},
};
