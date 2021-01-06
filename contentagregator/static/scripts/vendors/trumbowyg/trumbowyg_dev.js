$("#trumbowyg").trumbowyg({
	btns: [
		["historyUndo","historyRedo", "fontfamily", "fontsize"],
		["bold", "italic", "underline", "foreColor"],			
		["justifyLeft", "justifyCenter", "justifyRight", "justifyFull"],
		["unorderedList", "orderedList", "template", "removeformat"]
	],
	plugins: {
		templates: [
			{
				name: "Template 1",
				html: "<p>I am a template!</p>"
			},
			{
				name: "Template 2",
				html: "<p>I am a different template!</p>"
			}
		]
	}
});