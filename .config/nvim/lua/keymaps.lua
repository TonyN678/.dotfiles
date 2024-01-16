-- make shorter map command
-- use keymap.set because it allows set a function in many modes
local Map = vim.keymap.set

local opts = { noremap = true, silent = true }

-- Set leader key
vim.g.mapleader = " "

-- Basic movements between windows (Control + h/j/k/l)
Map({"n", "i"}, "<C-h>", "<C-w>h", opts)
Map({"n", "i"}, "<C-j>", "<C-w>j", opts)
Map({"n", "i"}, "<C-k>", "<C-w>k", opts)
Map({"n", "i"}, "<C-l>", "<C-w>l", opts)

-- resize windows/buffers (Control + Arrow keys)
Map({"n", "i"}, "<C-Up>", ":resize -2<CR>", opts)
Map({"n", "i"}, "<C-Down>", ":resize +2<CR>", opts)
Map({"n", "i"}, "<C-Left>", ":vertical resize -2<CR>", opts)
Map({"n", "i"}, "<C-Right>", ":vertical resize +2<CR>", opts)

-- Using H/L to go to the begining and the end of line
-- Note: H will map to _ (the first non-whitespace character of a line)
-- It would be helpful if it is a indent line in some languages like Python, Ruby, YAML, ...
Map('n', 'H', '_', defaults)
Map('n', 'L', '$', defaults)

