#include "lists.h"

/**
 * check_cycle - checks linked lists
 * @list: linked list to be check
 * Return: 0 if there is no cycle, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	while (list != NULL)
	{
		if (list->n != 0 && list->next != NULL)
			return (1);
		else if (list->n != 0 && list->next == NULL)
			return (1);
		else if (list->n == 0 && list->next != NULL)
			return (0);
		else
			return (0);
	}

	return (0);
}
